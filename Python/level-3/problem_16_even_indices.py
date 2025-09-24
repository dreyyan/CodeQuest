# ============================
# LEVEL 3 : [ Problem # 16 - Even Indices ]
# Define a function that takes a list and returns elements at even indices only.
# ============================
def even_indices(lst):
    # your code goes here
    lenght = len(lst)

    temp_number = 0

    list = []
    while (temp_number < lenght):

        if (temp_number % 2 != 0):
            list.append(temp_number)
        temp_number += 1

    list.sort(reverse=True)

    for item in list:
        lst.pop(item)

    return lst
    pass

# TEST CASES
print(even_indices([1, 2, 3, 4]))    # Output: [1, 3]
print(even_indices([5]))             # Output: [5]
print(even_indices([]))    
print(even_indices([10, 20, 30, 40]))              # Output: []