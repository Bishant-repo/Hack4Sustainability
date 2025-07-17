# 🌱 GreenTrack - Carbon Footprint Tracker

A full-stack web application inspired by Klima for personal carbon footprint tracking and offset platform. Built with Flask, MySQL, and modern web technologies.

## 🚀 Features

### 🔐 User Authentication
- Secure user registration and login
- Password hashing for security
- Session-based authentication
- User profile management

### 🧭 Onboarding Questionnaire
- Personalized lifestyle assessment
- Travel habits analysis (car, bus, walk, bike)
- Diet preferences (vegetarian, non-vegetarian, mixed)
- Energy usage evaluation (low, medium, high)
- Base carbon score calculation

### 📊 Interactive Dashboard
- Real-time carbon footprint display
- Visual charts using Chart.js
- Weekly/monthly emission trends
- Personalized climate tips
- Activity tracking statistics
- Quick action buttons

### 📝 Daily Activity Logging
- Transport mode tracking
- Meal type logging
- Energy usage monitoring
- Real-time carbon impact calculation
- Historical activity view

### 🌳 Carbon Offset Pledges
- Multiple pledge types (tree planting, renewable energy, carbon projects)
- Impact calculator
- Pledge history tracking
- Environmental impact visualization

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **JavaScript** - Interactive features and real-time calculations
- **Bootstrap 5** - Responsive design framework
- **Chart.js** - Data visualization
- **Font Awesome** - Icons

### Backend
- **Flask** - Python web framework
- **MySQL** - Database management
- **Flask-MySQLdb** - Database connector
- **Werkzeug** - Security utilities

### Database
- **MySQL** - Relational database
- **Multiple tables**: users, onboarding, daily_logs, pledges, climate_tips

## 📋 Prerequisites

Before running GreenTrack, ensure you have:

- **Python 3.8+** installed
- **MySQL Server** running
- **pip** package manager
- **Git** (for cloning)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd GreenTrack
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database

#### Option A: Using MySQL Command Line
```bash
mysql -u root -p
```

Then run the SQL commands from `database_setup.sql`:
```sql
CREATE DATABASE IF NOT EXISTS greentrack;
USE greentrack;
-- ... (rest of the SQL commands)
```

#### Option B: Using MySQL Workbench
1. Open MySQL Workbench
2. Connect to your MySQL server
3. Open `database_setup.sql`
4. Execute the script

### 5. Configure Application

Edit `app.py` to match your MySQL configuration:
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'greentrack'
```

### 6. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📖 Usage Guide

### For New Users

1. **Register** - Create a new account with your email and password
2. **Complete Onboarding** - Answer lifestyle questions to get your base carbon score
3. **Log Daily Activities** - Track your transport, meals, and energy usage
4. **Monitor Progress** - View your carbon footprint trends on the dashboard
5. **Make Pledges** - Offset your emissions by supporting environmental projects

### For Returning Users

1. **Login** - Access your personalized dashboard
2. **Log Activities** - Record today's activities
3. **View Trends** - Check your carbon footprint progress
4. **Make Pledges** - Continue supporting environmental initiatives

## 🗄️ Database Schema

### Users Table
- `id` - Primary key
- `name` - User's full name
- `email` - Unique email address
- `password` - Hashed password
- `created_at` - Registration timestamp

### Onboarding Table
- `id` - Primary key
- `user_id` - Foreign key to users
- `travel_habits` - Transport preference
- `diet` - Dietary preference
- `energy_usage` - Energy consumption level
- `base_score` - Calculated base carbon score

### Daily Logs Table
- `id` - Primary key
- `user_id` - Foreign key to users
- `transport_mode` - Mode of transport used
- `transport_distance` - Distance traveled
- `meal_type` - Type of meal consumed
- `energy_usage` - Energy consumption level
- `total_emissions` - Calculated CO₂ emissions
- `created_at` - Log timestamp

### Pledges Table
- `id` - Primary key
- `user_id` - Foreign key to users
- `amount` - CO₂ amount to offset
- `pledge_type` - Type of offset project
- `status` - Pledge status (pending/completed/cancelled)
- `created_at` - Pledge timestamp

### Climate Tips Table
- `id` - Primary key
- `title` - Tip title
- `content` - Tip description
- `category` - Tip category
- `impact_score` - Impact rating

## 🔧 Configuration

### Environment Variables
You can set these environment variables for production:

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key
export MYSQL_HOST=your-mysql-host
export MYSQL_USER=your-mysql-user
export MYSQL_PASSWORD=your-mysql-password
export MYSQL_DB=greentrack
```

### Carbon Calculation Factors
The application uses realistic carbon emission factors:

- **Transport**: Car (0.2 kg/km), Bus (0.05 kg/km), Train (0.04 kg/km)
- **Diet**: Vegetarian (0.5 kg/meal), Non-veg (2.5 kg/meal), Mixed (1.5 kg/meal)
- **Energy**: Low (2 kg/day), Medium (5 kg/day), High (10 kg/day)

## 🎯 Features in Detail

### Carbon Footprint Calculation
- Real-time calculation based on user activities
- Weighted average of recent logs
- Base score from onboarding questionnaire
- Dynamic updates with new data

### Data Visualization
- Line charts showing weekly trends
- Color-coded emission categories
- Interactive charts with Chart.js
- Responsive design for all devices

### User Experience
- Modern, intuitive interface
- Real-time form validation
- Helpful tips and guidance
- Progress tracking and achievements

## 🔒 Security Features

- Password hashing with Werkzeug
- Session-based authentication
- SQL injection prevention
- Input validation and sanitization
- Secure cookie handling

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set up a production MySQL server
2. Configure environment variables
3. Use a WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
4. Set up a reverse proxy (Nginx/Apache)
5. Configure SSL certificates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by Klima's carbon tracking approach
- Built with modern web technologies
- Designed for environmental awareness
- Created for educational and practical use

## 📞 Support

For support or questions:
- Create an issue in the repository
- Check the documentation
- Review the code comments

---

**Make a positive impact on our planet, one step at a time! 🌍** 