""" ============================
LEVEL 4 : [ Problem #5 - Count Vowels ]
Define a function that takes a string, counts
the # of vowels, and displays the vowel count.
============================ """
def count_vowels(string):
    # your code goes here
    vowels = "aeiouAEIOU"
    number_of_vowels = 0
    for char in string:
        if char in vowels:
            number_of_vowels += 1
    return number_of_vowels
    pass

# TEST CASES
print(count_vowels("hello"))      # Output: 2
print(count_vowels("rhythm"))     # Output: 0
print(count_vowels("AEiouXYZ"))   # Output: 5