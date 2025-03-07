#1.Function for arithmetic operators
def arithmetic_operations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b  

    print("Addition:", add)
    print("Subtraction:", sub)
    print("Multiplication:", mul)
    print("Division:", div)

arithmetic_operations(10, 5)

#2.Method for increment and decrement operators
x=5
# Increment
x += 1  
print("After increment:", x)
# Decrement
x -= 1  
print("After decrement:", x)


#3.Program to find the two numbers equal or not.
A = 30
B = 30
if A == B:
    print("Numbers are equal")
else:
    print("Numbers are not equal")

#4.Program for relational operators
a = 20 
b = 30

#Relational operators
print("a < b:", a < b)
print("a <= b:", a <= b)
print("a > b:", a > b)
print("a >= b:", a >= b)

#5.Print the smaller and larger number 
a = 30
b = 20
if a < b:
        print("Smaller number:", a)
        print("Larger number:", b)
else:
        print("Smaller number:", b)
        print("Larger number:", a)
