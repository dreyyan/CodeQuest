""" ============================
LEVEL 4 : [ Problem #8 - Check Anagram ]
Define a function that checks if two strings are anagrams of each other
(contain the same characters with the same frequency, ignoring case).
============================ """
def check_anagram(s, t):
    # your code goes here
    s = s.lower()
    t = t.lower()
    
    if (sorted(s) == sorted(t)):
        return True
    else:
        return False

# TEST CASES
print(check_anagram("anagram", "nagaram")) # Output: True
print(check_anagram("rat", "car"))         # Output: False
print(check_anagram("listen", "silent"))   # Output: True
