""" ============================
LEVEL 2 : [ Problem #6 - Multiplication Table ]
1. Ask the user to enter any number (n).
2. Print its multiplication table (1 - 12).
============================ """
# your code goes here

number = int(input("Enter number: "))

for i in range(1, 13): #minumum, and maximum. Remember iteration starts in 0.
    print(f"{number} x {i} = {number * i}")
