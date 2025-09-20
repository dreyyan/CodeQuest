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

number = int(input("Enter number: "))
sum = 0
for i in range(1,number+1): 
    print(i, end=" ")
    if number == i: # if number = 4, 4==4. print blank space after 4.
        print("", end="")
    else: 
        print("+ ",end="")
    sum += i

print(f"= {sum}")
# for the last iteration of the loop, dont print the number.
# if last iteration dont add plus sign, else add the plus sign