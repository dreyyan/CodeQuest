# ============================
# LEVEL 3 : [ Problem #14 - Contains Digit ]
# Define a function that takes a string and returns true if it contains any digit, false otherwise.
# ============================
def contains_digit(text):
    # your code goes here
    for i in range(1, 10):
        if str(i) in text:
            return True
    return False

    
                

# TEST CASES
print(contains_digit("hello2a"))    # Output: True
print(contains_digit("hello"))     # Output: False
print(contains_digit("123"))       # Output: True