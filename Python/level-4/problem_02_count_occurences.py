""" ============================
LEVEL 4 : [ Problem #2 - Count Occurrences ]
Define a function that takes a string and a character,
and returns the number of times the character appears.
============================ """
def count_occurrences(string, char):
    # your code goes here
    duplicate = 0
    
    for letters in string:

        if char in letters:
            duplicate += 1

    return duplicate

    pass

# TEST CASES
print(count_occurrences("hello", "l"))    # Output: 2
print(count_occurrences("banana", "a"))   # Output: 3
print(count_occurrences("test", "z"))     # Output: 0