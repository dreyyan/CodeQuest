/* ============================
LEVEL 1 : [ Problem #9 - Mini Receipt ]
1. Declare and initialize variables for:
   - Store Name
   - Item Name
   - Quantity
   - Price per item
2. Compute the total cost using arithmetic operations.
3. Display a receipt using template literals.
4. Make sure to use newline characters (\n) for proper formatting.
============================ */
// your code goes here

// declaration and iniatialization of vars
let storeName = 'Edz nilagaan';
let itemName = 'pancit';
let quantity = 10;
let pricePerItem = 50;

//declare and initilazed to 0
let total = 0;

// assigns product of quantity and price per item to var total
total = quantity * pricePerItem;

// prints information
console.log("======= STORE RECIEPT =======");
console.log(`Store: ${storeName}\n`);
console.log(`Item: ${itemName}`);
console.log(`Quantity: ${quantity}`);
console.log(`Price per item: ₱${pricePerItem}\n`);
console.log(`Total: ₱${total}`);
console.log("=============================");


/* Example Expected Output:
====== STORE RECEIPT ======
Store: Techie Supplies

Item: Notebook
Quantity: 3
Price per item: ₱50

Total: ₱150
===========================
*/