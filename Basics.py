#1.Program to print your name
print("Naveena")

#2.Program for a Single line comment and multi-line comments 
# This is a single-line comment

"""
This is a multi-line comment.
It contains multiple lines.
"""

#3.Define variables for different Data Types and print them
# Defining variables
int_var = 10       
bool_var = True    
char_var  = 'A'     
float_var = 10.5   
double_var = 20.1234  

# Printing values
print("Integer:", int_var)
print("Boolean:", bool_var)
print("Character:", char_var)
print("Float:", float_var)
print("Double:", double_var)

#4.Define the local and Global variables with the same name and print both variables
variables = "Global Variable"

def my_function():
    variables = "Local Variable"
    print("Inside function:", variables)  

my_function()
print("Outside function:", variables)  


