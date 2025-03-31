uimport mysql.connector
import hashlib

# Database connection and setup - (Sydney Erik Wamalwa)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = db.cursor()

# Create Database and Tables with enhanced structure
cursor.execute("CREATE DATABASE IF NOT EXISTS eduaccess")
cursor.execute("USE eduaccess")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(255) NOT NULL,
    lesson VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    UNIQUE(subject, lesson)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS quizzes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lesson VARCHAR(255) NOT NULL,
    question TEXT NOT NULL,
    answer VARCHAR(255) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS progress (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    lesson VARCHAR(255) NOT NULL,
    score INT NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)
""")
db.commit()

# Enhanced sample data with comprehensive content - (Sydney Erik Wamalwa)
def insert_sample_data():
    courses = [
        ("Mathematics", "Algebra Basics", 
        """Algebra Fundamentals:
1. Variables and Constants: Represent unknown values with letters (e.g., x, y)
2. Basic Equations: Solve 2x + 5 = 15 → x = 5
3. Linear Equations: Graph y = 2x + 3
4. Polynomials: (x + 2)(x + 3) = x² + 5x + 6"""),

        ("Mathematics", "Geometry Essentials",
        """Geometry Basics:
1. Angles: Right angle = 90°, Straight angle = 180°
2. Pythagorean Theorem: a² + b² = c²
3. Area Calculations:
   - Square: side²
   - Circle: πr²
4. Volume: Cube = side³"""),

        ("Science", "Physics Principles",
        """Core Physics Concepts:
1. Newton's Laws:
   - 1st Law: Inertia
   - 2nd Law: F = ma
   - 3rd Law: Action-Reaction
2. Energy Types: Kinetic, Potential
3. Ohm's Law: V = IR"""),

        ("Science", "Chemistry Basics",
        """Introduction to Chemistry:
1. Atoms: Proton, Neutron, Electron
2. Periodic Table Elements:
   - H (Hydrogen)
   - O (Oxygen)
   - C (Carbon)
3. Chemical Equations: 2H₂ + O₂ → 2H₂O"""),

        ("History", "World War II Overview",
        """WWII Key Points:
1. Timeline: 1939-1945
2. Major Powers:
   - Allies: USA, UK, USSR
   - Axis: Germany, Japan, Italy
3. Significant Events:
   - D-Day (1944)
   - Atomic Bombings (1945)""")
    ]

    for subject, lesson, content in courses:
        cursor.execute("""
        INSERT IGNORE INTO courses (subject, lesson, content)
        VALUES (%s, %s, %s)
        """, (subject, lesson, content))
    
    db.commit()

def insert_quiz_data():
    quizzes = [
        ("Algebra Basics", "Solve for x: 3x + 5 = 20", "5"),
        ("Algebra Basics", "Expand (x + 4)(x + 2)", "x²+6x+8"),
        ("Geometry Essentials", "Calculate area of circle with radius 3 (π=3.14)", "28.26"),
        ("Geometry Essentials", "Right triangle sides: 3cm and 4cm. Hypotenuse?", "5"),
        ("Physics Principles", "Calculate force (F=ma): m=10kg, a=2m/s²", "20"),
        ("Physics Principles", "Voltage with I=2A and R=5Ω (V=IR)", "10"),
        ("Chemistry Basics", "Number of atoms in H₂O molecule", "3"),
        ("Chemistry Basics", "Balance: _H₂ + O₂ → _H₂O", "2H2+O2→2H2O"),
        ("World War II Overview", "WWII start year", "1939"),
        ("World War II Overview", "Country that dropped atomic bombs in 1945", "USA")
    ]

    for lesson, question, answer in quizzes:
        cursor.execute("""
        INSERT IGNORE INTO quizzes (lesson, question, answer)
        VALUES (%s, %s, %s)
        """, (lesson, question, answer))
    
    db.commit()

# Initialize sample data
insert_sample_data()
insert_quiz_data()
#Security functions - (Nzabinesha Merci)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#Your code goes here team
#lumumba
# Progress tracking - (fadhili lumumba Nzabinesha Merci)
def update_progress(username, lesson, score):
    cursor.execute("""
    INSERT INTO progress (username, lesson, score)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE score = GREATEST(score, %s)
    """, (username, lesson, score, score))
    db.commit()

def show_progress(username):
    cursor.execute("""
    SELECT lesson, score FROM progress
    WHERE username = %s
    ORDER BY lesson
    """, (username,))

    print("\nLearning Progress:")
    for lesson, score in cursor:
        print(f"- {lesson}: {'★' * (score//20)}{'☆' * (5 - score//20)} ({score}%)")

# User registration
def register_user():
    while True:
        username = input("Create username (min 4 chars): ")
        if len(username) < 4:
            print("Username too short!")
            continue

        password = input("Create password (min 6 chars): ")
        if len(password) < 6:
            print("Password too weak!")
            continue

        try:
            cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, hash_password(password))
        )  # Closing parenthesis for cursor.execute
            db.commit()  # Ensure this is outside the execute method
            print("Registration successful!")
            return
        except mysql.connector.IntegrityError:
            print("Username already exists!")



# Main application flow - (Sydney Erik Wamalwa)
def main_menu():
    current_user = None
    while True:
        print("\nEDUACCESS LEARNING PORTAL")
        print("1. Register")
        print("2. Login")
        print("3. Browse Courses")
        print("4. Start Learning")
        print("5. View Progress")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            current_user = login()
        elif choice == "3":
            show_courses()
        elif choice == "4":
            if not current_user:
                print("Please login first!")
                continue

            show_courses()
            subject = input("Choose subject: ")
            cursor.execute("""
            SELECT lesson FROM courses
            WHERE subject = %s
            ORDER BY lesson
            """, (subject,))

            lessons = cursor.fetchall()
            if not lessons:
                print("Invalid subject selection!")
                continue

            print(f"\nAvailable Lessons in {subject}:")
            for i, (lesson,) in enumerate(lessons, 1):
                print(f"{i}. {lesson}")

            try:
                lesson_choice = int(input("Select lesson number: ")) - 1
                selected_lesson = lessons[lesson_choice][0]
            except:
                print("Invalid lesson selection!")
                continue

            if display_lesson_content(selected_lesson):
                input("\nPress Enter to start quiz...")
                score = take_quiz(selected_lesson)
                update_progress(current_user, selected_lesson, score)
        elif choice == "5":
            if current_user:
                show_progress(current_user)
            else:
                print("Please login first!")
        elif choice == "6":
            print("Thank you for learning with EduAccess!")
            break
        else:
            print("Invalid selection!")

if __name__ == "__main__":
    main_menu()
