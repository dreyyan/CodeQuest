""" ============================
LEVEL 3 : [ Problem #9 - Perfect Number Check ]
Define a function that takes a positive integer n and returns true if it is a perfect number,
i.e., the sum of its proper divisors (excluding n itself) equals n.
============================ """
def isPerfectNumber(n):
    # your code goes here
    list_of_divisibles = []
    temp_number2 = 0
    array = []

    for temp_number1 in range (1, n):
        
        if (n % temp_number1 == 0):
            list_of_divisibles.append(temp_number1)

    lenght = len(list_of_divisibles)
    sum = 0

    while (temp_number2 < lenght):
        array.append(int(list_of_divisibles[temp_number2]))
        sum += int(list_of_divisibles[temp_number2])
        temp_number2 += 1

    if (sum == n):
        print(*array, sep= " + ", end = " ") 
        print(" = " + str(sum))
        return True
    else:
        return False
    
    pass
# TEST CASES
print(isPerfectNumber(6))   # Output: True (1 + 2 + 3 = 6)
print(isPerfectNumber(28))  # Output: True (1 + 2 + 4 + 7 + 14 = 28)
print(isPerfectNumber(12))  # Output: False