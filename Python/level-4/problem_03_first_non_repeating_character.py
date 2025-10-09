""" ============================
LEVEL 4 : [ Problem #3 - First Non-Repeating Character ]
Define a function that returns the first non-repeating character in a string.
If none exists, return an empty string.
============================ """
def first_non_repeating_character(s):
    # your code goes here
    dictionary = {}
    for char in s:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    for char in s:
        if dictionary[char] == 1:
            return char
    return "\"\""
    
        

        
        

# TEST CASES
print(first_non_repeating_character("leetcode"))        # Output: "l"
print(first_non_repeating_character("aabb"))            # Output: ""
print(first_non_repeating_character("loveleetcode"))    # Output: "v"