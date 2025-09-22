""" ============================
LEVEL 3 : [ Problem #7 - Max in List ]
Define a function that takes a list of numbers
and returns the largest number.
============================ """
def max_in_list(nums):
    # your code goes here
    lenght_of_list = len(nums)
    temp_number1 = 0
    highest_number = nums[0]

    while (temp_number1 < lenght_of_list):
        
        if (highest_number < nums[temp_number1]):

            highest_number = nums[temp_number1]
        temp_number1 += 1

    return highest_number
    pass

# TEST CASES
print(max_in_list([3, 7, 2, 9, 5]))    # Output: 9
print(max_in_list([-10, -3, -25, -1])) # Output: -1
print(max_in_list([42]))               # Output: 42