/* ============================
LEVEL 1 : [ Problem #8 - Weekly Allowance ]
1. Declare and initialize a variable for your weekly allowance.
2. Declare and initialize variables for the following expenses:
    a. Food
    b. Transportation
    c. School Expenses
3. Use arithmetic operations (+, -, *, /) to calculate your remaining money 
   that will be allocated for savings.
4. Fix the template literals so they display the correct information.
============================ */
// your code goes here

// declaration and iniatialization of vars

let weeklyAllowance = 1000;

let foodExpense = 300;

let transpoExpense = 0;

let schoolExpense = 200;

//prints information
console.log(`I have a weekly allowance of ${weeklyAllowance}.`)
console.log(`I spend ${foodExpense} on food...`)
console.log(`I spend ${transpoExpense} on transportation...`)
console.log(`I spend ${schoolExpense} on school expenses...`)
console.log(`So, I am left with ${weeklyAllowance - foodExpense - transpoExpense - schoolExpense} for my savings.`)