# ============================
# LEVEL 3 : [ Problem # 16 - Even Indices ]
# Define a function that takes a list and returns elements at even indices only.
# ============================
def even_indices(lst):
    # your code goes here
    lenght = len(lst)

    temp_number = 0

    result = []
    while (temp_number < lenght):

        if (temp_number % 2 == 0):
            result.append(lst[temp_number])
        temp_number += 1


    return result
    pass

# TEST CASES
print(even_indices([1, 2, 3, 4]))    # Output: [1, 3]
print(even_indices([5]))             # Output: [5]
print(even_indices([]))              # Output: []