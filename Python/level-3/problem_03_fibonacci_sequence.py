""" ============================
LEVEL 3 : [ Problem #3 - Fibonacci Sequence ]
Define a function that takes an integer `n` and returns a
list of the first `n` numbers in the fibonacci sequence.
============================ """
def fibonacci_sequence(n):
    temp_number1 = 0
    temp_number2 = 0
    temp_number3 = 1
    temp_number4 = 0
    set = []
    while (temp_number1 < n):
        temp_number1 += 1
        set.append(temp_number2)
        temp_number2 += temp_number3
        temp_number3 = temp_number4
        temp_number4 = temp_number2
    return set
    pass

# TEST CASES
print(fibonacci_sequence(5))   # Output: [0, 1, 1, 2, 3]
print(fibonacci_sequence(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci_sequence(1))   # Output: [0]