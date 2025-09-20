""" ============================
LEVEL 2 : [ Problem #9 - FizzBuzz ]
1. Ask the user to enter any number (n).
2. Using conditionals and loops:
    a. If divisible by 3, print "Fizz"
    b. If divisible by 5, print "Buzz"
    c. If divisible by 3 and 5, print "FizzBuzz"
    d. Otherwise, print the number

[ EXAMPLE ]
Input:
n = 15

Output:
n = 1 -> 1
n = 2 -> 2
n = 3 -> "Fizz"
n = 4 -> 4
n = 5 -> "Buzz"
...
n = 15 -> "FizzBuzz"
============================ """
# your code goes here

number = int(input("Enter number: "))

for i in range(1, number+1):
    print(f"n = {i} ->", end=" ")
    if i % 3 == 0 and i % 5 == 0:
        print('"FizzBuzz"')
    elif i % 3 == 0:
        print('"Fizz"')
    elif i % 5 == 0:
        print('"Buzz"')
    else:
        print(i)