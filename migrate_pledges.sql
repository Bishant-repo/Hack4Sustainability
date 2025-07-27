-- Migration script to add payment_method and total_cost columns to pledges table
-- Run this if you have an existing database

USE greentrack;

-- Add new columns to pledges table
ALTER TABLE pledges 
ADD COLUMN payment_method VARCHAR(50) DEFAULT NULL AFTER status,
ADD COLUMN total_cost DECIMAL(10,2) DEFAULT NULL AFTER payment_method;

-- Update existing carbon_offset pledges to have default values
UPDATE pledges 
SET payment_method = 'card', total_cost = amount / 100 
WHERE pledge_type = 'carbon_offset' AND payment_method IS NULL; 