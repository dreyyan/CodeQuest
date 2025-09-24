# ============================
# LEVEL 3 : [ Problem #12 - Double String ]
# Define a function that takes a string and returns it repeated twice.
# ============================
def double_string(text):
    # your code goes here
    return text + text 
    pass

# TEST CASES
print(double_string("hi"))        # Output: "hihi"
print(double_string(""))          # Output: ""
print(double_string("python"))    # Output: "pythonpython"