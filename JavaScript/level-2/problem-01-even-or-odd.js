/* ============================
LEVEL 2 : [ Problem #1 - Even or Odd ]
1. Ask the user to input a number.
2. Use a conditional statement to check:
    a. If the number is even, display "{n} is even."
    b. If the number is odd, display "{n} is odd."
============================ */
// your code goes here

function solve(){

    let n = document.getElementById("num").value;

if(n % 2 == 0){
    console.log(`${n} is even.`);
}
else{
    console.log(`${n} is odd.`);
}
}