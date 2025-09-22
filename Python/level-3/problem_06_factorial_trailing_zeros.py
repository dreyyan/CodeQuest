""" ============================
LEVEL 3 : [ Problem #6 - Factorial Trailing Zeros ]
Define a function that takes a non-negative integer n and returns the number of trailing zeros in n! (n factorial).
============================ """
def trailingZeros(n):
    # your code goes here
    temp_number1 = 0
    factorial = 1
    digits = []
    temp_number2 = 0
    number_of_0 = 0

    while (temp_number1 < n):
        temp_number1 += 1
        factorial *= temp_number1

    for d in str(factorial):    
        digits.append(d)
        
    lenght_of_list = len(digits)

    digits.reverse()

    while (temp_number2 < lenght_of_list): 
        if (int(digits[temp_number2])  == 0):
            number_of_0 += 1
        else:
            break

        temp_number2 += 1

    answer = (f"{number_of_0} ({n}! = {factorial})")

    return answer
    pass

# TEST CASES
print(trailingZeros(5))   # Output: 1 (5! = 120)
print(trailingZeros(10))  # Output: 2 (10! = 3628800)
print(trailingZeros(0))   # Output: 0 (0! = 1)
print(trailingZeros(7))