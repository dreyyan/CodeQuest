# ============================
# LEVEL 3 : [ Problem #20 - Rotate List ]
# Define a function that takes a list and a number k, and rotates the list to the right by k positions.
# ============================
def rotate_list(lst, k):
    # your code goes here
    temp_number = 0
    while (temp_number < k):
        lst.reverse()
        temp_number += 1
    return lst    
    pass
# TEST CASES
print(rotate_list([1, 2, 3, 4], 1))    # Output: [4, 1, 2, 3]
print(rotate_list([1, 2, 3], 0))       # Output: [1, 2, 3]
print(rotate_list([], 5))              # Output: []