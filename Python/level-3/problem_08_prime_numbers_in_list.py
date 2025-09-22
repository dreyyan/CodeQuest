""" ============================
LEVEL 3 : [ Problem #8 - Prime in List ]
Define a function that takes an integer `n` and
returns the list of prime numbers from 1 to `n`.
============================ """
def prime_in_list(nums):
    # your code goes here
    temp_number1 = 0
    temp_number2 = 0
    check_prime = 0
    list_of_prime = []

    while (temp_number1 < nums):
        check_prime = 0
        temp_number2 = 0
        temp_number1 += 1
        while (temp_number2 < temp_number1):
            temp_number2 += 1
            if (temp_number1 % temp_number2 == 0):
                check_prime += 1
        if (check_prime == 2):
            list_of_prime.append(temp_number1)
    return list_of_prime
    pass

# TEST CASES
print(prime_in_list(10))  # Output: [2, 3, 5, 7]
print(prime_in_list(1))   # Output: []
print(prime_in_list(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]