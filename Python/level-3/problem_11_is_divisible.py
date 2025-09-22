# ============================
# LEVEL 3 : [ Problem #11 - Is Divisible ]
# Define a function that takes two numbers and returns true if the first is divisible by the second, false otherwise.
# ============================
def is_divisible(a, b):
    # your code goes here
    return a % b == 0
   
    pass

# TEST CASES
print(is_divisible(10, 2))    # Output: True
print(is_divisible(15, 4))    # Output: False
print(is_divisible(0, 5))     # Output: True