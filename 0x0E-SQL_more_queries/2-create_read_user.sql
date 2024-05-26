-- Script to create database hbtn_0d_2 and user user_0d_2 with SELECT privilege
-- Create the database if it doesn't exist
-- Create the user if it doesn't exist
-- Grant SELECT privilege on hbtn_0d_2 database to user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
