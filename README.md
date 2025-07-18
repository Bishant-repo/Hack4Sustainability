# 🌱 GreenTrack - Carbon Footprint Tracker
GreenTrack is a modern, gamified web application designed to help users track, reduce, and offset their carbon footprint in an engaging and insightful way. Built to support **SDG 13: Climate Action**, this app encourages individuals to become more environmentally conscious through daily habits and challenges.

## 🌟 Key Features

### 📊 Personal Carbon Footprint Tracker
- Log daily activities like transportation, diet, and energy use
- Calculate and visualize your carbon emissions in real-time
- Track your progress over time with detailed analytics

### 🎮 Gamified Experience
- Earn points and maintain streaks for sustainable actions
- Unlock badges and achievements as you reduce your impact
- Compete with yourself and others on the leaderboard

### 💡 Personalized Eco-Tips
- Get intelligent suggestions tailored to your behavior
- Receive actionable advice to help reduce your environmental impact
- Learn about sustainable practices through interactive tips

### 🌳 Offset Options
- Pledge to offset your emissions via tree-planting
- Support verified climate projects and renewable energy initiatives
- Make donations to environmental organizations

### 🧠 Educational Content
- "Did You Know?" facts section with climate trivia
- Learn surprising facts about environmental impact
- Stay informed and inspired with daily eco-facts

## 🎯 Sustainable Development Goal Alignment

This project directly aligns with multiple UN Sustainable Development Goals:

- **SDG 13 – Climate Action**: Empowers individuals to take measurable action against climate change
- **SDG 11 – Sustainable Cities & Communities**: Encourages sustainable urban living practices
- **SDG 3 – Good Health & Well-being**: Promotes healthier lifestyle choices through sustainable habits

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package installer)



## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: MySQL with Flask-MySQLdb
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Werkzeug password hashing
- **Styling**: Custom CSS with modern, responsive design

## 📁 Project Structure

```
greentrack/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── database_setup.sql    # Database schema and sample data
├── setup.py             # Installation script
├── static/
│   └── css/
│       └── eco.css      # Custom styling
└── templates/
    ├── base.html        # Base template
    ├── index.html       # Landing page
    ├── login.html       # Login page
    ├── register.html    # Registration page
    ├── dashboard.html   # Main dashboard
    ├── log.html         # Activity logging
    ├── pledge.html      # Offset pledges
    ├── profile.html     # User profile
    └── onboarding.html  # User onboarding
```

## 🔧 Configuration

### Database Configuration
Update the MySQL configuration in `app.py`:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'greentrack'
```

### Environment Variables (Recommended for Production)
Create a `.env` file for sensitive configuration:

```env
SECRET_KEY=your_secret_key_here
MYSQL_HOST=localhost
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DB=greentrack
```

## 📊 Carbon Calculation Methodology

The application uses industry-standard carbon factors:

- **Transport**: Car (0.2 kg CO2/km), Bus (0.05 kg CO2/km), Train (0.04 kg CO2/km)
- **Diet**: Vegetarian (0.5 kg CO2/meal), Non-vegetarian (2.5 kg CO2/meal), Mixed (1.5 kg CO2/meal)
- **Energy**: Low (2 kg CO2/day), Medium (5 kg CO2/day), High (10 kg CO2/day)

## 🎮 How to Use

1. **Registration & Onboarding**
   - Create an account with your email
   - Complete the onboarding questionnaire to set your baseline
   - Get personalized recommendations based on your lifestyle

2. **Daily Tracking**
   - Log your daily activities (transport, meals, energy usage)
   - View your carbon footprint in real-time
   - Track your progress and improvements

3. **Gamification**
   - Earn points for sustainable choices
   - Maintain streaks for consistent eco-friendly behavior
   - Unlock badges and achievements

4. **Offsetting**
   - Pledge to offset your carbon footprint
   - Choose from tree planting, renewable energy, or carbon offset projects
   - Track your positive impact


## 🙏 Acknowledgments

- UN Sustainable Development Goals for inspiration
- The open-source community for tools and libraries
- Environmental organizations for carbon calculation methodologies
- All contributors who help make this project better

## 📞 Support

- **Email**: bidaribishant07@gmail.com

## 🌍 Impact

Every small action counts! By using GreenTrack, you're:
- Becoming more aware of your environmental impact
- Making informed decisions about your daily choices
- Contributing to global climate action goals
- Inspiring others to live more sustainably

---

**Make a positive impact on our planet, one step at a time! 🌍**
 