# 🎓 Student Fee Management System

A web-based fee management system built with **Flask** and **MySQL** that allows students to submit fee payments and staff to view and manage all payment records.

---

## 📸 Overview

| Role | What they can do |
|------|-----------------|
| 👨‍🎓 Student | Fill fee payment form, get instant receipt |
| 👨‍💼 Staff | Login, view all payments, search by enrollment |

---

## 🚀 Features

- 📋 Student fee submission form with all details
- 🧾 Automatic payment receipt generation
- 🔐 Staff login portal
- 📊 View all payment records with total collected amount
- 🔍 Search student payment details by enrollment number
- 🔒 Credentials secured via `.env` file (never hardcoded)
- 🛡️ Parameterized SQL queries (no SQL injection)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, Flask 3.0 |
| Database | MySQL |
| Frontend | HTML5, CSS3 |
| Security | python-dotenv |

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/CODESSOHAM/Student-Fee-Management-System.git
cd Student-Fee-Management-System
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file in the root folder

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=student_management

### 4. Set up the MySQL database
```sql
CREATE DATABASE student_management;

USE student_management;

CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment VARCHAR(50),
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(100),
    stream VARCHAR(100),
    year INT,
    semester INT,
    fees_for VARCHAR(100),
    amount FLOAT,
    date DATE,
    section VARCHAR(10),
    roll_no INT,
    bank_branch VARCHAR(100),
    account_number VARCHAR(50),
    utr_number VARCHAR(50)
);
```

### 5. Run the application
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📁 Project Structure

Student-Fee-Management-System/
│
├── app.py                  # Main Flask application & routes
├── db_config.py            # Database connection (uses .env)
├── requirements.txt        # Project dependencies
├── .env                    # Secret credentials (NOT tracked by git)
├── .gitignore              # Git ignored files
│
├── templates/              # HTML templates (Jinja2)
│   ├── index.html          # Home page
│   ├── student_form.html   # Fee submission form
│   ├── payment_receipt.html# Receipt after payment
│   ├── staff_login.html    # Staff login page
│   ├── staff_dashboard.html# Staff dashboard
│   ├── view_all.html       # All payments table
│   └── student_details.html# Student search result
│
└── static/                 # CSS and static assets

---

## 🔐 Security Practices

- ✅ Database credentials stored in `.env` — never committed to GitHub
- ✅ `.gitignore` prevents accidental secret exposure
- ✅ All SQL queries use parameterized statements to prevent injection
- ✅ `__pycache__` excluded from version control

---

## 🗺️ Application Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/student` | GET, POST | Fee submission form |
| `/staff` | GET, POST | Staff login |
| `/staff_dashboard` | GET | Staff dashboard |
| `/view_all` | GET | View all payments |
| `/student_details` | GET, POST | Search by enrollment |

---

## 👨‍💻 Author

**Soham** — [GitHub @CODESSOHAM](https://github.com/CODESSOHAM)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
