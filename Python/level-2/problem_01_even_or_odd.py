""" ============================
LEVEL 2 : [ Problem #1 - Even or Odd ]
1. Ask the user to input a number.
2. Use a conditional statement to check:
    a. If the number is even, display "{n} is even."
    b. If the number is odd, display "{n} is odd."
============================ """
# your code goes here

number = int(input("Enter a number: "))

if number % 2 == 0:
    print (f"{number} is even.")
else:
    print (f"{number} is odd")