# ============================
# LEVEL 3 : [ Problem #19 - Sum of Nested List ]
# Define a function that takes a nested list of numbers and returns the sum of all numbers.
# ============================
def sum_nested_list(nested):
    # your code goes here
    sum = 0
    for list1 in nested:
        for list2 in list1:
            sum += list2
    return sum 
    pass

# TEST CASES
print(sum_nested_list([[1, 2], [3], [4, 5]]))    # Output: 15
print(sum_nested_list([[], []]))                  # Output: 0
print(sum_nested_list([[1], [2, 3]]))            # Output: 6