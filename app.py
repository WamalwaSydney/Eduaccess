class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
users = []

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users.append(User(username, password))
    print("Registration successful!")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    for user in users:
        if user.username == username and user.password == password:
            print("Login successful!")
            return True
    print("Invalid username or password.")
    return False
