""" ============================
LEVEL 1 : [ Problem #9 - Mini Receipt ]
1. Declare and initialize variables for:
   - Store Name
   - Item Name
   - Quantity
   - Price per item
2. Compute the total cost using arithmetic operations.
3. Display a receipt using f-strings.
4. Make sure to use newline characters (\n) for proper formatting.
============================ """
# your code goes here

store_name = "Mr DIY" # Store Name
item_name = "Screwdriver Set" # Item Name
quantity = 2 # Quantity
price_per_item = 350 # Price per item in PHP

total_cost = quantity * price_per_item # Compute total cost

print(f"====== STORE RECEIPT ====== \nStore: {store_name}") #prints the receipt
print(" ")
print(f"Item: {item_name} \nQuantity: {quantity} \nPrice per item: {price_per_item}")
print(" ")
print(f"Total: {total_cost} \n===========================")

''' Example Expected Output:
====== STORE RECEIPT ======
Store: Techie Supplies

Item: Notebook
Quantity: 3
Price per item: ₱50

Total: ₱150
===========================
'''