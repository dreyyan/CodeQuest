/* ============================
LEVEL 2 : [ Problem #7 - Sum of First n ]
1. Ask the user to enter any number (n).
2. Use a loop to compute the sum of the first `n` numbers.

[ EXAMPLE ]
Input:
n = 4

Output:
1 + 2 + 3 + 4 = 10
============================ */
// your code goes here

async function sum(){

    let num = document.getElementById("n").value;

    let sum = 0;

    for (let i = 1; i <= num; i++){

        sum += i;

        console.log( i + ' + ');
    }

    console.log(' = ' + sum)
}