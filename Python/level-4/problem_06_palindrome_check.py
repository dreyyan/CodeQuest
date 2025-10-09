""" ============================
LEVEL 4 : [ Problem #6 - Palindrome Check ]
Define a function that takes a string:
    a. If word is palindrome, return `True`
    b. Otherwise, return `False`
============================ """
def palindrome_check(string):
    # your code goes here
    uppercase = string.upper()
    if (uppercase == uppercase[::-1]):
        return True
    else:
        return False
            
            

# TEST CASES
print(palindrome_check("racecar"))  # Output: True
print(palindrome_check("hello"))    # Output: False
print(palindrome_check("Madam"))    # Output: True