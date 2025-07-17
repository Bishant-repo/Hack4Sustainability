#!/usr/bin/env python3
"""
GreenTrack Setup Script
This script helps set up the GreenTrack application by:
1. Installing dependencies
2. Setting up the database
3. Creating initial configuration
"""

import sys
import subprocess
import mysql.connector
from mysql.connector import Error


def print_banner():
    """Print the GreenTrack banner"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🌱 GreenTrack Setup                      ║
    ║              Carbon Footprint Tracking System                ║
    ╚══════════════════════════════════════════════════════════════╝
    """)


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required.")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print("✅ Python version check passed")


def install_dependencies():
    """Install required Python packages"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Error: Failed to install dependencies")
        sys.exit(1)


def get_mysql_config():
    """Get MySQL configuration from user"""
    print("\n🗄️  MySQL Database Configuration")
    print("Please provide your MySQL connection details:")
    
    host = input("MySQL Host (default: localhost): ").strip() or "localhost"
    user = input("MySQL Username (default: root): ").strip() or "root"
    password = input("MySQL Password: ").strip()
    database = (input("Database Name (default: greentrack): ").strip() 
                or "greentrack")
    
    return {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }


def test_mysql_connection(config):
    """Test MySQL connection"""
    print("\n🔗 Testing MySQL connection...")
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password']
        )
        if connection.is_connected():
            print("✅ MySQL connection successful")
            connection.close()
            return True
    except Error as e:
        print(f"❌ MySQL connection failed: {e}")
        return False


def setup_database(config):
    """Set up the database and tables"""
    print("\n🗄️  Setting up database...")
    
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password']
        )
        
        cursor = connection.cursor()
        
        # Create database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
        print(f"✅ Database '{config['database']}' created/verified")
        
        # Use the database
        cursor.execute(f"USE {config['database']}")
        
        # Read and execute SQL setup script
        with open('database_setup.sql', 'r') as file:
            sql_commands = file.read()
        
        # Split and execute commands
        commands = sql_commands.split(';')
        for command in commands:
            command = command.strip()
            if command:
                cursor.execute(command)
        
        connection.commit()
        print("✅ Database tables created successfully")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"❌ Database setup failed: {e}")
        return False
    
    return True


def update_app_config(config):
    """Update the app.py file with MySQL configuration"""
    print("\n⚙️  Updating application configuration...")
    
    try:
        with open('app.py', 'r') as file:
            content = file.read()
        
        # Update MySQL configuration
        content = content.replace(
            "app.config['MYSQL_HOST'] = 'localhost'",
            f"app.config['MYSQL_HOST'] = '{config['host']}'"
        )
        content = content.replace(
            "app.config['MYSQL_USER'] = 'root'",
            f"app.config['MYSQL_USER'] = '{config['user']}'"
        )
        content = content.replace(
            "app.config['MYSQL_PASSWORD'] = ''",
            f"app.config['MYSQL_PASSWORD'] = '{config['password']}'"
        )
        content = content.replace(
            "app.config['MYSQL_DB'] = 'greentrack'",
            f"app.config['MYSQL_DB'] = '{config['database']}'"
        )
        
        with open('app.py', 'w') as file:
            file.write(content)
        
        print("✅ Application configuration updated")
        
    except Exception as e:
        print(f"❌ Failed to update configuration: {e}")
        return False
    
    return True


def create_env_file(config):
    """Create a .env file for environment variables"""
    print("\n📝 Creating environment file...")
    
    env_content = f"""# GreenTrack Environment Variables
FLASK_ENV=development
SECRET_KEY=greentrack_secret_key_2024
MYSQL_HOST={config['host']}
MYSQL_USER={config['user']}
MYSQL_PASSWORD={config['password']}
MYSQL_DB={config['database']}
"""
    
    try:
        with open('.env', 'w') as file:
            file.write(env_content)
        print("✅ Environment file created (.env)")
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")


def main():
    """Main setup function"""
    print_banner()
    
    print("Welcome to GreenTrack Setup!")
    print("This script will help you configure the application.\n")
    
    # Check Python version
    check_python_version()
    
    # Install dependencies
    install_dependencies()
    
    # Get MySQL configuration
    config = get_mysql_config()
    
    # Test MySQL connection
    if not test_mysql_connection(config):
        print("\n❌ Setup failed. Please check your MySQL configuration.")
        sys.exit(1)
    
    # Setup database
    if not setup_database(config):
        print("\n❌ Database setup failed.")
        sys.exit(1)
    
    # Update app configuration
    if not update_app_config(config):
        print("\n❌ Configuration update failed.")
        sys.exit(1)
    
    # Create environment file
    create_env_file(config)
    
    print("\n" + "="*60)
    print("🎉 GreenTrack Setup Complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Run the application: python app.py")
    print("2. Open your browser: http://localhost:5000")
    print("3. Register a new account and start tracking!")
    print("\nFor more information, see README.md")
    print("\nHappy carbon tracking! 🌱")


if __name__ == "__main__":
    main() 