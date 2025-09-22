""" ============================
LEVEL 2 : [ Problem #6 - Multiplication Table ]
1. Ask the user to enter any number (n).
2. Print its multiplication table (1 - 12).
============================ """
# your code goes here

num = int(input("Input any number: "))# Ask User for Input

for a in range (1, 13):#Condition for loop
 print(f"{num} * {a} = {num * a}")




