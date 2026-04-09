import haslib
import getpass

def hash_passwprd (password):
    return hashlib.sha256(password.encode()).hexigest()

users = {"user1": hash_password("password1"), "user2": hash_password("password2")}

def login():
    username = input("Enter your username: ")
    password = getpass.getpassinput("Enter your password: ")
    
    if username in users and users[username] == hash_password(password):
        print("Login successful!")
        return True
    else:
        print("Invalid Credentials.")
        return False
  

# Example usage
login()
