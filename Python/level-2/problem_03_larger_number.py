""" ============================
LEVEL 2 : [ Problem #3 - Larger Number ]
1. Ask the user to input two numbers.
2. Use a conditional statement to determine which number is larger.
3. Display the larger number.
============================ """
# your code goes here

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    print(f"{num1} is larger than {num2}")
else:
    print(f"{num2} is larger than {num1}")