""" ============================
LEVEL 3 : [ Problem #2 - Check Prime ]
1. Define a function that:
    a. If prime, returns `True`
    o. Otherwise, returns `False`
============================ """
def check_prime(n):
      temp_number1 = 0
      check_prime = 0
      for temp_number1 in range (1, n + 1):
            if (n % temp_number1 == 0):
                  check_prime += 1
      if (check_prime == 2):
            return True
      else:
            return False
    

# TEST CASES
print(check_prime(2))   # Output: True
print(check_prime(15))  # Output: False
print(check_prime(17))  # Output: True