# 🌱 GreenTrack - Carbon Footprint Tracker

GreenTrack is a modern, gamified web application designed to help users track, reduce, and offset their carbon footprint in an engaging and insightful way. Built to support **SDG 13: Climate Action**, this app encourages individuals to become more environmentally conscious through daily habits and challenges.

## 🌟 Key Features

### 📊 Personal Carbon Footprint Tracker
- **Daily Activity Logging**: Track transportation, diet, and energy usage
- **Real-time Calculations**: Instant carbon footprint updates based on your activities
- **Trend Analysis**: Visualize your emissions over time with interactive charts
- **Smart Scoring**: Dynamic carbon score that reflects your actual daily impact

### 🎮 Gamified Experience
- **Activity Streaks**: Maintain daily logging streaks for consistent tracking
- **Progress Tracking**: Visual indicators of your sustainability journey
- **Achievement System**: Unlock milestones as you reduce your environmental impact

### 💡 Personalized Eco-Tips
- **Smart Recommendations**: Get tips tailored to your lifestyle and habits
- **Actionable Advice**: Practical suggestions to reduce your carbon footprint
- **Educational Content**: Learn about sustainable practices and their impact

### 🌳 Carbon Offset with Credits
- **Credit System**: Purchase carbon credits at $10 per 1,000 kg CO₂
- **Multiple Payment Options**: Credit Card, PayPal, and Cryptocurrency support
- **Project Transparency**: See exactly where your offset money goes
- **Verified Projects**: Support tree planting, renewable energy, and efficiency projects
- **Payment Tracking**: Monitor your offset pledges and payment status

### 🧠 Interactive Learning
- **"Did You Know?" Section**: Climate facts and trivia with source links
- **Quiz Mode**: Test your environmental knowledge with interactive quizzes
- **Educational Resources**: Links to authoritative climate information sources

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

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Hack4sustainability
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   mysql -u your_username -p < database_setup.sql
   ```

4. **Configure the application**
   - Update MySQL settings in `app.py`
   - Set your database credentials

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and go to `http://127.0.0.1:5000`
   - Register a new account and start tracking your carbon footprint!



## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: MySQL with Flask-MySQLdb
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Charts**: Chart.js for data visualization
- **Styling**: Custom CSS with modern, responsive design


## 📁 Project Structure

```
Hack4sustainability/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── database_setup.sql       # Database schema and sample data
├── migrate_pledges.sql      # Database migration for payment features
├── setup.py                 # Installation script
├── static/
│   └── css/
│       └── eco.css          # Custom styling
└── templates/
    ├── base.html            # Base template with Bootstrap
    ├── index.html           # Landing page
    ├── login.html           # Login page
    ├── register.html        # Registration page
    ├── dashboard.html       # Main dashboard with charts
    ├── log.html             # Activity logging
    ├── pledge.html          # Offset pledges
    ├── profile.html         # User profile
    └── onboarding.html      # User onboarding
```



## 📊 Carbon Calculation Methodology

The application uses industry-standard carbon factors based on verified environmental research:

### **Transport Emissions**
- **Car**: 0.2 kg CO₂/km
- **Bus**: 0.05 kg CO₂/km  
- **Train**: 0.04 kg CO₂/km
- **Motorcycle**: 0.15 kg CO₂/km
- **Airplane**: 0.255 kg CO₂/km (average short-haul flight)
- **Walk/Bike**: 0 kg CO₂/km (sustainable options)

### **Diet Emissions**
- **Vegetarian**: 0.5 kg CO₂/meal
- **Non-vegetarian**: 2.5 kg CO₂/meal
- **Mixed**: 1.5 kg CO₂/meal

### **Energy Usage**
- **Low**: 2 kg CO₂/day
- **Medium**: 5 kg CO₂/day
- **High**: 10 kg CO₂/day

### **Dynamic Scoring System**
- **Real-time Updates**: Carbon score updates based on recent logged activities
- **7-Day Average**: Uses the last 7 days of data for current score calculation
- **Trend Analysis**: Weekly emission trends for long-term progress tracking

## 🎮 How to Use

### 1. **Registration & Onboarding**
   - Create an account with your email
   - Complete the onboarding questionnaire to set your baseline
   - Get personalized recommendations based on your lifestyle

### 2. **Daily Tracking**
   - Log your daily activities (transport, meals, energy usage)
   - View your carbon footprint in real-time with dynamic scoring
   - Track your progress with interactive charts and trends

### 3. **Carbon Offset with Credits**
   - Click "Offset with Credits" on your dashboard
   - Choose from preset options (1, 5, or full annual credits) or custom amount
   - Select your preferred payment method (Credit Card, PayPal, Cryptocurrency)
   - Complete your pledge to support verified environmental projects

### 4. **Interactive Learning**
   - Explore the "Did You Know?" section for climate facts
   - Test your knowledge with interactive quizzes
   - Learn about sustainable practices and their impact

### 5. **Progress Monitoring**
   - View your weekly emission trends
   - Track your offset pledges and payment status
   - Monitor your sustainability journey with visual indicators


## 🙏 Acknowledgments

- **UN Sustainable Development Goals** for inspiration and guidance
- **Carbon Footprint Ltd** for carbon calculation methodologies
- **The open-source community** for tools and libraries
- **Environmental organizations** for verified project information
- **All contributors** who help make this project better

## 📞 Support & Contact

- **Contact Email**: bidaribishant07@gmail.com
-                     unesh.khadka22@gmail.com

## 🌍 Impact & Mission

Every small action counts! By using GreenTrack, you're:
- **Becoming more aware** of your environmental impact
- **Making informed decisions** about your daily choices
- **Contributing to global climate action** goals (SDG 13)
- **Supporting verified environmental projects** through carbon offsets
- **Inspiring others** to live more sustainably

---

**Make a positive impact on our planet, one step at a time! 🌍**

*Built with ❤️ for a sustainable future*
 