""" ============================
LEVEL 2 : [ Problem #4 - Simple Login ]
1. Declare variables for username and password.
2. Initialize any username or password that you want.
3. Ask the user to enter a username and password.
4. Check if the username and password match the correct credentials:
    a. If correct, display "Login successful!"
    b. If incorrect, display "Invalid username or password."
============================ """
# your code goes here

username = "JC"
password = 12345

user_name = input("Enter username: ")
pass_word = int(input("Enter password: "))

if (user_name == username and pass_word == password):
    print("Login successful")
else:
    print("Invalid")
