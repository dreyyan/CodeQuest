/* ============================
LEVEL 2 : [ Problem #3 - Larger Number ]
1. Ask the user to input two numbers.
2. Use a conditional statement to determine which number is larger.
3. Display the larger number.
============================ */
// your code goes here

async function larger()
{
     let n = document.getElementById("num1").value;
     let m = document.getElementById("num2").value;

    if (n > m){
        console.log(n)
    }
    else {
        console.log(m)
    }
}

