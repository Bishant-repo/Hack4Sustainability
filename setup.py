from MySQLdb import IntegrityError, OperationalError

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        industry_id = request.form['industry_id']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cur.fetchone():
            flash('Email already registered!', 'error')
            return render_template('register.html')

        hashed_password = generate_password_hash(password)
        try:
            cur.execute(
                "INSERT INTO users (name, email, password, industry_id) VALUES (%s, %s, %s, %s)",
                (name, email, hashed_password, industry_id)
            )
            mysql.connection.commit()
        except IntegrityError:
            flash('Email already registered! (IntegrityError)', 'error')
            return render_template('register.html')
        except OperationalError as e:
            if e.args[0] == 1054:
                flash('Unknown column \'industry_id\' in \'field list\'', 'error')
                return render_template('register.html')
        finally:
            cur.close()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html') 