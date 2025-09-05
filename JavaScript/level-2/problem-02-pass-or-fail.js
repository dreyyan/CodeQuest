/* ============================
LEVEL 2 : [ Problem #2 - Pass or Fail ]
1. Ask the user to input a grade in percentage (%).
2. Use a conditional statement to check:
    a. If the grade is 75 or higher, display "You passed!"
    b. Otherwise, display "You failed, better luck next time..."
============================ */
// your code goes here
async function determinegrade()
{
     let n = document.getElementById("num").value;

    if (n >= 75){
        console.log ('You passed!')
    }
    else {
        console.log ('You failed, better luck next time...')
    }
}