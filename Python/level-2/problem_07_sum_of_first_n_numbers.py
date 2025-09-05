""" ============================
LEVEL 2 : [ Problem #7 - Sum of First n ]
1. Ask the user to enter any number (n).
2. Use a loop to compute the sum of the first `n` numbers.

[ EXAMPLE ]
Input:
n = 4

Output:
1 + 2 + 3 + 4 = 10
============================ """
# your code goes here

num = int(input("Enter Number: ")) #Ask User for Input
tempNum = 0
sum = 0

for tempNum in range (1, num + 1,):
    sum += tempNum
    print()
    

"""

space = ""


while tempNum < num:
    tempNum += 1
    sum += tempNum
    print(f"{tempNum}", f"{space}", sep=' + ',end="")

print(f"= {sum}")

"""
    
    




    

