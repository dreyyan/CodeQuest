/* ============================
LEVEL 2 : [ Problem #6 - Multiplication Table ]
1. Ask the user to enter any number (n).
2. Print its multiplication table (1 - 12).
============================ */
// your code goes here

async function multiply(){

    let n = document.getElementById("num").value;

for (let i = 1; i < 13 ; i++){

    console.log(n * i);
}

}