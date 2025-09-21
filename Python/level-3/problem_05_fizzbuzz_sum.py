""" ============================
LEVEL 3 : [ Problem #5 - FizzBuzz Sum ]
Define a function that takes a positive integer n and returns the sum of all numbers from 1 to n
that are divisible by 3 or 5 (inclusive of n).
============================ """
def fizzBuzzSum(n):
    # your code goes here
    temp_number1 = 0
    sum = 0
    while (temp_number1 < n):
        temp_number1 += 1
        
        if (temp_number1 % 3 == 0 or temp_number1 % 5 == 0):
            sum += temp_number1
    return sum
    pass

# TEST CASES
print(fizzBuzzSum(15))  # Output: 60 (3 + 5 + 6 + 9 + 10 + 12 + 15)
print(fizzBuzzSum(5))   # Output: 8 (3 + 5)
print(fizzBuzzSum(2))   # Output: 0