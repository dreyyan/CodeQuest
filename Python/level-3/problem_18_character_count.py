# ============================
# LEVEL 3 : [ Problem #18 - Character Count ]
# Define a function that takes a string and returns a dictionary with the count of each character.
# ============================
def char_count(text):
    # your code goes here
    list = []
    first = 0
    second = 0
    duplicates = 0
    dictionary = {}

    for char in text:
        list.append(char)
        
    lenght = len(list)

    while (first < lenght):

        second = 0

        while (second < lenght):

            if (list[first] == list[second]):

                duplicates += 1
                second += 1
            else: 
                second += 1

        dictionary[list[first]] = duplicates

        duplicates = 0

        first += 1
    return dictionary
        
    

# TEST CASES
print(char_count("hello"))    # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(char_count("aaa"))      # Output: {'a': 3}
print(char_count(""))         # Output: {}

