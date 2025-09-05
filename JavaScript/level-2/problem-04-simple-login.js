/* ============================
LEVEL 2 : [ Problem #4 - Simple Login ]
1. Declare variables for username and password.
2. Initialize any username or password that you want.
3. Ask the user to enter a username and password.
4. Check if the username and password match the correct credentials:
    a. If correct, display "Login successful!"
    b. If incorrect, display "Invalid username or password."
============================ */
// your code goes here

async function signin(){
    
let userName = 'Mj';
let pass = '123';

let n = document.getElementById("username").value;
let m = document.getElementById("password").value;

if (userName === n && pass === m){
    console.log ('Log in Successful!')
}
else {
    console.log ('Invalid username or Password')
}
}

