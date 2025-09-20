""" ============================
LEVEL 2 : [ Problem #10 - Student Grading System ]
1. Ask the user to enter 5 grades in percentage (%).
2. For each grade, determine the letter equivalent using conditionals:
    a. 90 or above  -> "A"
    b. 80–89        -> "B"
    c. 70–79        -> "C"
    d. 60–69        -> "D"
    e. Below 60     -> "F"
3. Display the grade and its corresponding letter.

[ EXAMPLE ]
Input:
85

Output:
Grade: 85 -> B
============================ """
# your code goes here

for i in range(1,6):
    grade = int(input("Enter 5 grades in percentage (%): "))
    if grade >= 90:
        print(f"Grade: {grade} -> A")
        print(end="\n")
    elif grade >= 80:
        print(f"Grade: {grade} -> B")
        print(end="\n")
    elif grade >= 70:
        print(f"Grade: {grade} -> C")
        print(end="\n")
    elif grade >= 60:
        print(f"Grade: {grade} -> D")
        print(end="\n")
    else:
        print(f"Grade: {grade} -> F")
        print(end="\n")




