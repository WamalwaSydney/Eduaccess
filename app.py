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
