# 🎓 Degree Evaluation - Project Setup

## 📌 Prerequisites
- Python 3 installed on  env
- Mysql installed on  env
- Django installed on  env
- Mysql-Client installed on env

## 🗄️ Database Setup
1. **Create a Mysql Database**
   - Name your new database `programeval`.
2. **Create a Mysql User**
   - Set up a user with a unique username and password.
   - Grant this user all privileges on the `programeval` database.

## 🔧 Virtual Environment
1. **Create a Virtual Environment**
   - Run `python3 -m venv env` to create a virtual environment.
2. **Activate the Virtual Environment**
   - On Linux/macOS, run `source env/bin/activate`.
   - On Windows, run `env\Scripts\activate`.

## 🌎 Environment setting
1. Open Program_Eval/setting.py, find DATABASES setting, modify the USER and PASSWORD as you set.
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

