# 🎓 Degree Evaluation - Project Setup

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Database Setup](#database-setup)
3. [Virtual Environment](#virtual-environment)
4. [Environment Variables](#environment-variables)
5. [Package Installation](#package-installation)
6. [Django Migrations](#django-migrations)
7. [Load Data](#load-data)
8. [Run the Server](#run-the-server)

## 📌 Prerequisites
- Python 3 installed on  env
- Mysql installed on  env
- Django installed on  env
- Mysql-Client installed on env

## 🗄️ Database Setup
1. **Create a PostgreSQL Database**
   - Name your new database `programeval`.
2. **Create a PostgreSQL User**
   - Set up a user with a unique username and password.
   - Grant this user all privileges on the `programeval` database.

## 🔧 Virtual Environment
1. **Create a Virtual Environment**
   - Run `python3 -m venv env` to create a virtual environment.
2. **Activate the Virtual Environment**
   - On Linux/macOS, run `source env/bin/activate`.
   - On Windows, run `env\Scripts\activate`.

## 🌎 Environment Variables
1. **Create a .env File**
   - This file should be placed next to this `README.md`.
2. **Add Database Environment Variables**
   - Include your PostgreSQL username, password, and port in the `.env` file.

## 📦 Package Installation
1. **Install All Required Packages**
   - Run `pip install -r requirements.txt`.

## ⚙️ Django Migrations
1. **Make Migrations**
   - Run `python3 manage.py makemigrations`.
2. **Run Migrations**
   - Execute `python3 manage.py migrate` to apply the migrations.

## 📊 Load Data
1. **Load Initial Data**
   - Execute `python3 manage.py loaddata university/fixtures/*.json`.

## 💻 Run the Server
1. **Start the Django Development Server**
   - Run `python3 manage.py runserver`.
   - Access the server through your preferred browser at `http://127.0.0.1:8000/`.

