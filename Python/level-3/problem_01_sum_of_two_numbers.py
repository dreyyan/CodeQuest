""" ============================
LEVEL 3 : [ Problem #1 - Sum of Two Numbers ]
1. Define a function that takes two numbers as input and returns their sum.
2. Then, call the function inside the print statement.
============================ """
a, b = 3, 5

def sum_of_two_numbers(a, b):
    # your code goes here
    sum = a + b
    return sum
    pass

print(f"{a} + {b} = {sum_of_two_numbers(a, b)}")