""" ============================
LEVEL 2 : [ Problem #8 - Factorial Calculator ]
1. Ask the user to enter any number (n).
2. Compute `n!` using a loop.

[ EXAMPLE ]
Input:
n = 5

Output:
5! = 5 x 4 x 3 x 2 x 1 = 120
============================ """
# your code goes here

number = int(input("Enter number: "))

multi = 1
print(f"{number}! =", end=" ")

for i in reversed(range(1, number+1)): #reversed - the order of your range, so it starts reading at 5
    print(i, end=" ")
    if i == 1: 
        print("", end="")
    else:
        print("x ", end="")
    multi *= i

print(f"= {multi}")

# I am not sure if my if statement is correct, I feel like I cheated the system.
