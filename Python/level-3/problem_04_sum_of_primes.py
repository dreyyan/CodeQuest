""" ============================
LEVEL 3 : [ Problem #4 - Sum of Primes ]
Define a function that takes a positive integer n and returns the sum of all prime numbers less than or equal to n.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
============================ """
def sumOfPrimes(n):
    # your code goes here
        temp_number1 = 0
        temp_number2 = 0
        check_prime = 0
        sum_of_prime = 0

        while (temp_number1 < n):
            check_prime = 0
            temp_number2 = 0
            temp_number1 += 1
            while (temp_number2 < temp_number1):
                temp_number2 += 1
                if (temp_number1 % temp_number2 == 0):
                    check_prime += 1
            if (check_prime == 2):
                sum_of_prime += temp_number1
        return sum_of_prime

                        
        
                        
                    




# TEST CASES
print(sumOfPrimes(10))  # Output: 17 (2 + 3 + 5 + 7)
print(sumOfPrimes(5))   # Output: 5 (2 + 3)
print(sumOfPrimes(2))   # Output: 2
