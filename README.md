# 🚀 CSV Upload & Processing System

## 📌 Project Description
This project is a web-based application built using Django that allows users to upload CSV files, process the data, and store it in a database. The processed data is then displayed in a structured and user-friendly table format.

---

## ✨ Features
- Upload CSV file through a web interface
- Validate file type (only CSV files are allowed)
- Parse CSV data using Python
- Store data in SQLite database
- Display records in a clean table format
- Prevent duplicate entries
- Handle empty rows and invalid inputs
- Error handling for robust performance
- Modern and responsive UI using Bootstrap

---

## 🛠️ Tech Stack
- Backend: Django (Python)
- Frontend: HTML, Bootstrap
- Database: SQLite
- Version Control: Git & GitHub

---

## ▶️ How to Run the Project

1. Clone the repository:
git clone https://github.com/vishhxl/csv-upload-system.git

2. Go inside project:
cd csvproject

3. Install Django:
pip install django

4. Run server:
python manage.py runserver

5. Open:
http://127.0.0.1:8000/

---

## 📄 CSV Format Example
name,email,age  
Vishal,vishal@gmail.com,21  
Rahul,rahul@gmail.com,22  

---

## 🎯 Usage
- Upload CSV from homepage
- View data at /data/

---

## 🔒 Validation
- Only CSV allowed
- Duplicate data prevented
- Empty rows skipped

---

## 📌 Author
Vishal Solanki
