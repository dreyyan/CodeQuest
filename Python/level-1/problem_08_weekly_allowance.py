""" ============================
LEVEL 1 : [ Problem #8 - Weekly Allowance ]
1. Declare and initialize a variable for your weekly allowance.
2. Declare and initialize variables for the following expenses:
    a. Food
    b. Transportation
    c. School Expenses
3. Use arithmetic operations (+, -, *, /) to calculate your remaining money 
   that will be allocated for savings.
4. Fix the f-strings so they display the correct information.
============================ """
# your code goes here

weekly_allowance = 500  # Weekly allowance
food_expense = 100 # Food expense
transportation_expense = 50 # Transportation expense
school_expense = 300 # School expense

remaining_money = weekly_allowance - (food_expense + transportation_expense + school_expense)  # Calculate remaining money


#Print Output
print(f"I have a weekly allowance of ₱{weekly_allowance}.")
print(f"I spend ₱{food_expense} on food...")
print(f"I spend ₱{transportation_expense} on transportation...")
print(f"I spend ₱{school_expense} on school expenses...")
print(f"So, I am left with ₱{remaining_money} for my savings.")