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

user_name = input("username: ") #Ask for User Input
user_password = input("password: ")

# data for password and username
data_username = "admin"
data_password = "12345"


if(user_name == data_username and user_password == data_password): 
    print(f"Login Successful")
else:
    print("Password and Username incorrect")

