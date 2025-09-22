""" ============================
LEVEL 2 : [ Problem #1 - Even or Odd ]
1. Ask the user to input a number.
2. Use a conditional statement to check:
    a. If the number is even, display "{n} is even."
    b. If the number is odd, display "{n} is odd."
============================ """
# your code goes here

a = int(input("Input number to see if its even or odd ")) # Ask User for input
even = a % 2

if(even == 0): #Condition for even
    print(f"{a} is even") 
else:
    print(f"{a} is odd")




