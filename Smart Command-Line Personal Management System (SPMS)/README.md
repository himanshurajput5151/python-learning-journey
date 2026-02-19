A modular, scalable Command-Line Personal Management System built using Python.
This project demonstrates clean backend architecture, structured development practices, and professional Git workflow.

The system allows users to manage authentication, expenses, tasks, and notes with persistent storage using JSON.

📌 Overview

This project was built to simulate real-world backend development without relying on external frameworks.

It focuses on:

Clean architecture

Separation of concerns

Modular code organization

Defensive file handling

Feature-based Git workflow

Incremental system expansion

✨ Core Features
🔐 Authentication

User Registration

Login via Username or Email

Duplicate user prevention

Persistent user storage

💰 Expense Management

Add expense

View expenses

Delete expense

User-specific expense tracking

📝 Task Management

Add tasks

View tasks

Manage task records

📒 Notes Management

Create notes

View notes

Persistent note storage

🏗 System Architecture

The application follows a layered structure:

SCLPMS/
│
├── main.py
├── config.py
│
├── factory_work/
│   ├── validator.py
│   └── file_handler.py
│
├── models/
│   ├── user.py
│   ├── expense.py
│   ├── task.py
│   └── note.py
│
├── services/
│   ├── auth_service.py
│   ├── expense_service.py
│   ├── task_service.py
│   └── note_service.py
│
└── data/
    ├── users.json
    ├── expenses.json
    ├── tasks.json
    └── notes.json

Design Principles Used

Single Responsibility Principle

Separation of Concerns

Layered Architecture

Modular Service-Based Design

Defensive Programming

Structured Git Branch Workflow

💾 Data Persistence

All data is stored locally using JSON files:

users.json

expenses.json

tasks.json

notes.json

The system safely handles:

Missing files

Corrupt JSON

Empty files

Automatic initialization

🛠 Technologies Used

Python 3

JSON

Regular Expressions (Validation)

Git & GitHub

🌿 Git Workflow

The project follows a professional branching model:

main → Stable and production-ready

Feature branches → Isolated development

Merging only after feature completion

Example workflow:

git checkout -b feature-expense-module
git add .
git commit -m "Implemented expense management"
git checkout main
git merge feature-expense-module

📦 Installation & Running
1️⃣ Clone the Repository
git clone <your-repository-link>

2️⃣ Navigate to Project Directory
cd SCLPMS

3️⃣ Run the Application
python main.py

🎯 Learning Outcomes

This project demonstrates:

Backend system thinking

Data modeling

Business logic separation

File handling best practices

Clean project structuring

Real-world Git usage

Iterative system design

🚀 Future Enhancements

Password Hashing (Security Upgrade)

SQLite / PostgreSQL Integration

Role-Based Access Control

Data Export (CSV / PDF)

CLI UI Improvements

Unit Testing Suite

Logging System

Docker Support

🤝 Contributing

Contributions are welcome.

Fork the repository

Create a new feature branch

Commit your changes

Submit a pull request

📄 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Himanshusingh Rajput

Backend-focused Python developer building structured, scalable systems from scratch.
