# EduAccess Learning Portal
EduAccess is a comprehensive online learning platform designed to deliver course content, quizzes, and progress tracking. The system supports user registration, login, course browsing, lesson content display, interactive quizzes, and progress monitoring—all integrated with a MySQL database.

Features
User Registration & Login:
Users can create accounts (with secure, hashed passwords) and log in to access course content.

Course Management:
The system supports multiple subjects and lessons, each with comprehensive course content.

Interactive Quizzes:
Each lesson includes an interactive quiz to test users’ understanding, with immediate feedback and score calculation.

Progress Tracking:
Users’ scores for each lesson are recorded and displayed as a progress report.

Sample Data:
Preloaded sample courses, lessons, and quiz questions make it easy to test the system.

Technology Stack
Backend: Python 3 with MySQL Connector

Database: MySQL

Security: Password hashing using SHA-256

Team Contributions
Sydney Erik Wamalwa:

Database connection and setup

Creating the database and tables

Inserting sample course and quiz data

Main application flow (main menu, navigation)

Nzabinesha Merci:

Security functions (password hashing)

Progress display (show_progress)

Aime Igirimpuhwe:

User registration with password validation

Quiz functionality (taking quizzes, scoring)

Fadhili Beracah Lumumba:

User authentication (login)

Progress tracking (updating progress using GREATEST for better score retention)

Setup Instructions
Prerequisites
Python 3 installed on your system.

MySQL Server installed and running.

mysql-connector-python package installed in your Python environment.

Installation Steps
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/eduaccess.git
cd eduaccess
Set up a virtual environment (optional but recommended):

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy
Edit
pip install mysql-connector-python
Set up MySQL:

Make sure your MySQL server is running.

Ensure that your MySQL credentials in the code are correct (default user is root with no password). If necessary, adjust the connection parameters in the script.

Run the application:

bash
Copy
Edit
python3 app.py
Usage
Registration:
Choose option 1 to register. Provide a username (minimum 4 characters) and password (minimum 6 characters).

Login:
Choose option 2 to log in. You will have three attempts before the login fails.

Browse Courses:
Option 3 lists the available subjects. Once you choose a subject, you can view its lessons.

Start Learning:
Option 4 allows you to select a lesson from a chosen subject. The lesson content is displayed, and then you can take the associated quiz.

View Progress:
Option 5 displays your progress in each lesson using a star rating system and percentage score.

Exit:
Option 6 quits the application.

Database Schema
The MySQL database eduaccess includes four main tables:

users:
Stores user data (ID, username, hashed password).

courses:
Contains course data including subject, lesson name, and lesson content. Each subject-lesson combination is unique.

quizzes:
Stores quiz questions and answers for each lesson.

progress:
Tracks the user’s highest score for each lesson. Uses a foreign key referencing the users table.

Contributing
Contributions are welcome! Follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix.

Commit your changes with clear messages.

Push your branch and open a pull request.

License
This project is licensed under the MIT License.

Contact
For questions, suggestions, or issues, please open an issue in the repository or contact the project team.
