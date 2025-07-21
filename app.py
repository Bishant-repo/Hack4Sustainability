from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'greentrack_secret_key_2024'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'greentrack'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Carbon footprint calculation factors (kg CO2 per unit)
CARBON_FACTORS = {
    'transport': {
        'car': 0.2,  # kg CO2 per km
        'bus': 0.05,
        'train': 0.04,
        'walk': 0,
        'bike': 0,
        'motorbike': 0.15  # kg CO2 per km (lower than car but higher than public transport)
    },
    'diet': {
        'veg': 0.5,  # kg CO2 per meal
        'non_veg': 2.5,
        'mixed': 1.5
    },
    'energy': {
        'low': 2,     # kg CO2 per day
        'medium': 5,
        'high': 10
    }
}


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()

        # Check if user already exists
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cur.fetchone():
            flash('Email already registered!', 'error')
            return render_template('register.html')

        # Hash password and insert user
        hashed_password = generate_password_hash(password)
        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password)
        )
        mysql.connection.commit()
        cur.close()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']

            # Check if user has completed onboarding
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM onboarding WHERE user_id = %s",
                (user['id'],)
            )
            onboarding = cur.fetchone()
            cur.close()

            if not onboarding:
                return redirect(url_for('onboarding'))
            else:
                return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password!', 'error')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/onboarding', methods=['GET', 'POST'])
def onboarding():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Always initialize wizard state if missing
    if 'onboarding_step' not in session or 'onboarding_answers' not in session:
        session['onboarding_step'] = 1
        session['onboarding_answers'] = {}

    step = session['onboarding_step']
    answers = session['onboarding_answers']
    progress = int((step - 1) / 3 * 100)
    base_score = None

    if request.method == 'POST':
        # Save answer for current step
        if step == 1 and 'travel_habits' in request.form:
            answers['travel_habits'] = request.form['travel_habits']
            session['onboarding_step'] = 2
        elif step == 2 and 'diet' in request.form:
            answers['diet'] = request.form['diet']
            session['onboarding_step'] = 3
        elif step == 3 and 'energy_usage' in request.form:
            answers['energy_usage'] = request.form['energy_usage']
            # Calculate base score
            base_score = calculate_base_score(
                answers['travel_habits'],
                answers['diet'],
                answers['energy_usage']
            )
            # Save to DB
            cur = mysql.connection.cursor()
            cur.execute(
                """
                INSERT INTO onboarding (user_id, travel_habits, diet, energy_usage, base_score, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    session['user_id'],
                    answers['travel_habits'],
                    answers['diet'],
                    answers['energy_usage'],
                    base_score,
                    datetime.now()
                )
            )
            mysql.connection.commit()
            cur.close()
            # Set to completion step
            session['onboarding_step'] = 4
            session['base_score'] = base_score
            return redirect(url_for('onboarding'))
        return redirect(url_for('onboarding'))

    # Show completion step if finished
    if step == 4 or session.get('onboarding_step') == 4:
        base_score = session.get('base_score', 0.0)
        # Show completion step ONCE, then clear onboarding session state and redirect to dashboard on next visit
        if session.get('onboarding_complete_shown'):
            session.pop('onboarding_step', None)
            session.pop('onboarding_answers', None)
            session.pop('base_score', None)
            session.pop('onboarding_complete_shown', None)
            return redirect(url_for('dashboard'))
        else:
            session['onboarding_complete_shown'] = True
            return render_template(
                'onboarding.html',
                step=4,
                progress=100,
                base_score=base_score
            )

    return render_template(
        'onboarding.html',
        step=step,
        progress=progress
    )


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    cur = mysql.connection.cursor()
    
    # Get user's current carbon score
    cur.execute("SELECT * FROM onboarding WHERE user_id = %s", (session['user_id'],))
    onboarding = cur.fetchone()
    
    # Get recent logs for charts
    cur.execute("""
        SELECT * FROM daily_logs 
        WHERE user_id = %s 
        ORDER BY created_at DESC 
        LIMIT 30
    """, (session['user_id'],))
    logs = cur.fetchall()
    
    # Convert Decimal values to float for template compatibility
    for log in logs:
        log['total_emissions'] = float(log['total_emissions'])
        log['transport_distance'] = float(log['transport_distance'])
    
    # Get user's pledges
    cur.execute("""
        SELECT * FROM pledges 
        WHERE user_id = %s 
        ORDER BY created_at DESC
    """, (session['user_id'],))
    pledges = cur.fetchall()
    
    # Convert Decimal values to float for template compatibility
    for pledge in pledges:
        pledge['amount'] = float(pledge['amount'])
    
    # Get climate tips
    cur.execute("SELECT * FROM climate_tips ORDER BY RAND() LIMIT 3")
    tips = cur.fetchall()
    
    cur.close()
    
    # Calculate current carbon score
    current_score = calculate_current_score(logs, onboarding['base_score'] if onboarding else 0.0)
    
    # Calculate weekly trend
    weekly_data = calculate_weekly_trend(logs)
    
    return render_template('dashboard.html', 
                         user_name=session['user_name'],
                         current_score=current_score,
                         logs=logs,
                         pledges=pledges,
                         tips=tips,
                         weekly_data=weekly_data)


@app.route('/log', methods=['GET', 'POST'])
def log_activity():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        transport_mode = request.form['transport_mode']
        transport_distance = float(request.form['transport_distance'])
        meal_type = request.form['meal_type']
        energy_usage = request.form['energy_usage']
        
        # Calculate carbon footprint for this log
        transport_emissions = CARBON_FACTORS['transport'][transport_mode] * transport_distance
        meal_emissions = CARBON_FACTORS['diet'][meal_type]
        energy_emissions = CARBON_FACTORS['energy'][energy_usage]
        
        total_emissions = transport_emissions + meal_emissions + energy_emissions
        
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO daily_logs (user_id, transport_mode, transport_distance, meal_type, 
                                  energy_usage, total_emissions, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (session['user_id'], transport_mode, transport_distance, meal_type, 
              energy_usage, total_emissions, datetime.now()))
        mysql.connection.commit()
        cur.close()
        
        flash('Activity logged successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('log.html')


@app.route('/pledge', methods=['GET', 'POST'])
def pledge():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        amount = float(request.form['amount'])
        pledge_type = request.form['pledge_type']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO pledges (user_id, amount, pledge_type, created_at)
            VALUES (%s, %s, %s, %s)
        """, (session['user_id'], amount, pledge_type, datetime.now()))
        mysql.connection.commit()
        cur.close()
        
        flash('Pledge submitted successfully!', 'success')
        return redirect(url_for('pledge'))
    
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT * FROM pledges 
        WHERE user_id = %s 
        ORDER BY created_at DESC
    """, (session['user_id'],))
    pledges = cur.fetchall()
    cur.close()
    
    # Convert Decimal values to float for template compatibility
    total_offset = 0
    for pledge in pledges:
        pledge['amount'] = float(pledge['amount'])
        total_offset += pledge['amount']
    
    return render_template('pledge.html', pledges=pledges, total_offset=total_offset)


@app.route('/api/score')
def get_score():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM onboarding WHERE user_id = %s", (session['user_id'],))
    onboarding = cur.fetchone()
    
    cur.execute("""
        SELECT * FROM daily_logs 
        WHERE user_id = %s 
        ORDER BY created_at DESC 
        LIMIT 30
    """, (session['user_id'],))
    logs = cur.fetchall()
    cur.close()
    
    current_score = calculate_current_score(logs, onboarding['base_score'] if onboarding else 0.0)
    
    return jsonify({'score': current_score})


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    # Fetch user info
    cur.execute("SELECT * FROM users WHERE id = %s", (session['user_id'],))
    user = cur.fetchone()

    # Fetch achievements/badges (stub: you can expand this logic)
    badges = []
    cur.execute("SELECT COUNT(*) as streak FROM daily_logs WHERE user_id = %s", (session['user_id'],))
    streak = cur.fetchone()['streak']
    if streak >= 7:
        badges.append({'icon': 'fa-fire', 'label': '7-Day Streak'})
    if streak >= 30:
        badges.append({'icon': 'fa-crown', 'label': '30-Day Streak'})

    # Preferences (stub: you can expand to use a preferences table)
    preferences = {'reminders': True, 'streak_alerts': True}

    message = None
    if request.method == 'POST':
        name = request.form.get('name', user['name'])
        email = request.form.get('email', user['email'])
        password = request.form.get('password', '')
        # Update user info
        if password:
            hashed_password = generate_password_hash(password)
            cur.execute(
                "UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s",
                (name, email, hashed_password, session['user_id'])
            )
        else:
            cur.execute(
                "UPDATE users SET name=%s, email=%s WHERE id=%s",
                (name, email, session['user_id'])
            )
        mysql.connection.commit()
        message = 'Profile updated successfully!'
        # Optionally update preferences here
        cur.execute("SELECT * FROM users WHERE id = %s", (session['user_id'],))
        user = cur.fetchone()
    cur.close()
    return render_template(
        'profile.html',
        user=user,
        badges=badges,
        preferences=preferences,
        message=message
    )


def calculate_base_score(travel_habits, diet, energy_usage):
    """Calculate base carbon score from onboarding data"""
    base_score = 0
    
    # Travel habits (daily average)
    if travel_habits == 'car':
        base_score += 5  # 25km daily average
    elif travel_habits == 'bus':
        base_score += 1.25
    elif travel_habits == 'train':
        base_score += 1
    elif travel_habits == 'walk':
        base_score += 0
    elif travel_habits == 'bike':
        base_score += 0
    
    # Diet (daily average)
    if diet == 'veg':
        base_score += 1.5
    elif diet == 'non_veg':
        base_score += 7.5
    elif diet == 'mixed':
        base_score += 4.5
    
    # Energy usage (daily average)
    if energy_usage == 'low':
        base_score += 2
    elif energy_usage == 'medium':
        base_score += 5
    elif energy_usage == 'high':
        base_score += 10
    
    return base_score


def calculate_current_score(logs, base_score):
    """Calculate current carbon score based on recent logs and base score"""
    if not logs:
        return float(base_score) if base_score else 0.0
    
    # Calculate average daily emissions from recent logs
    total_emissions = sum(float(log['total_emissions']) for log in logs)
    avg_daily_emissions = total_emissions / len(logs)
    
    # Combine with base score
    current_score = (float(base_score) + avg_daily_emissions) / 2
    
    return round(current_score, 2)


def calculate_weekly_trend(logs):
    """Calculate weekly emission trends for charts"""
    if not logs:
        return []
    
    # Group logs by week
    weekly_data = {}
    for log in logs:
        week_start = log['created_at'].date() - timedelta(days=log['created_at'].weekday())
        if week_start not in weekly_data:
            weekly_data[week_start] = []
        weekly_data[week_start].append(float(log['total_emissions']))
    
    # Calculate weekly averages
    trend_data = []
    for week_start, emissions in weekly_data.items():
        avg_emissions = sum(emissions) / len(emissions)
        trend_data.append({
            'week': week_start.strftime('%Y-%m-%d'),
            'emissions': round(avg_emissions, 2)
        })
    
    return trend_data


if __name__ == '__main__':
    app.run(debug=True) 