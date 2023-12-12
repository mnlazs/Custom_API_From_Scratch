DROP DATABASE IF EXISTS AstronomyAppDB;
CREATE DATABASE IF NOT EXISTS AstronomyAppDB;
USE AstronomyAppDB;

-- Script para crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL
);

-- Script para crear la tabla de preferencias de usuario
CREATE TABLE IF NOT EXISTS UserPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    FrequencyPreference VARCHAR(255),
    TimingPreference VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
