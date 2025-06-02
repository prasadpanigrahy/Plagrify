# Plagrification 🔍📄

Plagrification is a web-based plagiarism detection tool built with **Flask**.  
It allows users to register, log in, upload documents, compare multiple files, and view similarity scores — all in a clean, responsive UI with dark mode support.

---

## 🚀 Features

- 🔐 User Registration & Login (with flash messages)
- 📂 Upload and Compare Files
- 📊 View Similarity Scores and History
- ⚙️ Admin Panel to manage users and uploads
- 🌗 Dark/Light Theme Toggle
- 📅 "Last Compared" timestamps
- 🔍 Filter, Sort, and Export Results (PDF/TXT)
- 📬 Success/Error messages with Bootstrap alerts
- 🧠 Intelligent multi-file plagiarism checking

---

## 🛠️ Tech Stack

- **Backend**: Flask, SQLAlchemy, Jinja2
- **Frontend**: HTML, Bootstrap 5, JavaScript
- **Database**: SQLite (default, can be changed)
- **Deployment**: Render.com _(or your choice)_

---

## 📁 Project Structure

Plagrification/
├── backend/
│ ├── app.py
│ ├── auth.py
│ ├── checker.py
│ ├── admin.py
│ ├── models.py
│ ├── database.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── register.html
│ │ └── ...
│ └── static/
│ ├── styles.css
│ └── theme-toggle.js
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

````bash
git clone https://github.com/yourusername/Plagrification.git
cd backend

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3. Install Dependencies

```bash
pip install -r requirements.txt

### 4. Run the App

```bash
python app.py


📃 License
This project is licensed under the MIT License — see the LICENSE file for details.


🙌 Author
Developed by Prasad Panigrahy
Follow me on Twitter or connect on LinkedIn

````
