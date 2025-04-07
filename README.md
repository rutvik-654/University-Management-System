# 🎓 University Management System (Python CLI Project)

This is a simple **University Management System** built with Python, designed to manage colleges, students, and teachers through a **menu-driven command-line interface**.

## 🚀 Features

- Create new colleges
- Add students and teachers to colleges
- View all students or teachers in a college
- Search students or teachers by roll number
- Clear and interactive menu-based navigation

## 🧠 Concepts Used

- **Object-Oriented Programming (OOP)**
  - Inheritance
  - Class composition
- Python control structures
- CLI interaction using `input()` and loops

## 🏛️ Class Overview

- `Person`: Base class with roll number and name
- `Student`: Inherits `Person` and adds a branch
- `Teacher`: Inherits `Person` and adds a subject
- `College`: Manages lists of students and teachers and supports operations like add/search

## 🏗️ Project Structure

```bash
university-management-system/
├── main.py
└── README.md
▶️ How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/university-management-system.git
Navigate to the folder:

bash
Copy
Edit
cd university-management-system
Run the script:

bash
Copy
Edit
python main.py
📋 Sample Menu
markdown
Copy
Edit
Choose the Required option:
1. Create College.
2. Add Student.
3. Add Teacher.
4. Display Students.
5. Display Teachers.
6. Search Student by Roll No.
7. Search Teacher by Roll No.
8. Exit.
