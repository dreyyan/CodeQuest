# ============================
# LEVEL 3 : [ Problem #14 - Contains Digit ]
# Define a function that takes a string and returns true if it contains any digit, false otherwise.
# ============================
def contains_digit(text):
    # your code goes here
    for i in range(1, 10):
        index = text.find(str(i))
        print (index)
        if index != -1:
            return True
        else:
            return False

    
                

# TEST CASES
print(contains_digit("hello1a"))    # Output: True
print(contains_digit("hello"))     # Output: False
print(contains_digit("123"))       # Output: True