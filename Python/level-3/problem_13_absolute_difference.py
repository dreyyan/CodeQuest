# ============================
# LEVEL 3 : [ Problem #13 - Absolute Difference ]
# Define a function that takes two numbers and returns the absolute difference between them.
# ============================
def absolute_difference(a, b):  
    # your code goes here
        difference = a - b

        square = difference ** 2

        difference = square **  0.5

        return int(difference)


# TEST CASES
print(absolute_difference(5, 3))    # Output: 2
print(absolute_difference(3, 5))    # Output: 2
print(absolute_difference(0, 0))    # Output: 0