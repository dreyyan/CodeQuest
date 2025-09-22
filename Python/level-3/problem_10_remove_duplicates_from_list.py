""" ============================
LEVEL 3 : [ Problem #10 - Remove Duplicates From List ]
Define a function that takes a list of numbers and only returns
the unique elements.
============================ """
def remove_duplicates_from_list(nums):
    # your code goes here
    temp_number1 = 0
    temp_number2 = 1
    lenght = len(nums)

    while (temp_number1 < lenght - 1):

        temp_number2 = temp_number1 + 1

        while (temp_number2 < lenght):

            if (nums[temp_number1] == nums[temp_number2]):
                nums.pop(temp_number2)
                lenght = len(nums)
            else:
                temp_number2 += 1

        temp_number1 += 1

    return nums
    pass

# TEST CASES
print(remove_duplicates_from_list([1, 2, 2, 3, 4, 4, 2, 4]))      # Output: [1, 2, 3, 4]
print(remove_duplicates_from_list([5, 5, 5, 5]))            # Output: [5]
print(remove_duplicates_from_list([1, 2, 3, 4, 5]))         # Output: [1, 2, 3, 4, 5]