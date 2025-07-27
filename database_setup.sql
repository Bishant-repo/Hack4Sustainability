-- GreenTrack Database Schema
-- Run this script to create the database and tables

CREATE DATABASE IF NOT EXISTS greentrack;
USE greentrack;

-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Onboarding table
CREATE TABLE onboarding (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    travel_habits ENUM('car', 'bus', 'train', 'walk', 'bike', 'motorbike') NOT NULL,
    diet ENUM('veg', 'non_veg', 'mixed') NOT NULL,
    energy_usage ENUM('low', 'medium', 'high') NOT NULL,
    base_score DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Daily logs table
CREATE TABLE daily_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    transport_mode ENUM('car', 'bus', 'train', 'walk', 'bike', 'motorbike') NOT NULL,
    transport_distance DECIMAL(10,2) DEFAULT 0,
    meal_type ENUM('veg', 'non_veg', 'mixed') NOT NULL,
    energy_usage ENUM('low', 'medium', 'high') NOT NULL,
    total_emissions DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Pledges table
CREATE TABLE pledges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    pledge_type ENUM('tree_planting', 'renewable_energy', 'carbon_offset') NOT NULL,
    status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending',
    payment_method VARCHAR(50) DEFAULT NULL,
    total_cost DECIMAL(10,2) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Climate tips table
CREATE TABLE climate_tips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    category ENUM('transport', 'diet', 'energy', 'general') NOT NULL,
    impact_score INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample climate tips
INSERT INTO climate_tips (title, content, category, impact_score) VALUES
('Walk or Bike for Short Trips', 'Consider walking or biking for trips under 2km. This can reduce your carbon footprint by up to 2kg CO2 per trip.', 'transport', 3),
('Choose Plant-Based Meals', 'Replacing one meat meal with a plant-based option can save up to 2.5kg CO2 per meal.', 'diet', 4),
('Use Public Transport', 'Taking the bus instead of driving can reduce your emissions by up to 75% for the same journey.', 'transport', 4),
('Switch to LED Bulbs', 'Replacing traditional bulbs with LED can reduce energy consumption by up to 80%.', 'energy', 3),
('Reduce Food Waste', 'Plan your meals and store food properly to reduce waste. Food waste contributes to 8% of global emissions.', 'diet', 3),
('Unplug Electronics', 'Unplug chargers and electronics when not in use to reduce phantom energy consumption.', 'energy', 2),
('Choose Local Produce', 'Buying local fruits and vegetables reduces transportation emissions and supports local farmers.', 'diet', 2),
('Carpool When Possible', 'Sharing rides can reduce your transport emissions by up to 50% per trip.', 'transport', 3),
('Use Cold Water for Laundry', 'Washing clothes in cold water can save up to 90% of the energy used by your washing machine.', 'energy', 2),
('Reduce Single-Use Plastics', 'Bring your own water bottle and shopping bags to reduce plastic waste and emissions.', 'general', 2); 

-- Remove industry_id from users and drop industries table if exists
ALTER TABLE users DROP FOREIGN KEY IF EXISTS users_ibfk_industry_id;
ALTER TABLE users DROP COLUMN IF EXISTS industry_id;
DROP TABLE IF EXISTS industries; 