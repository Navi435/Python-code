#1.Program to print  “Bright IT Career”  ten times using for loop
for i in range(10):
    print("Bright IT Career")

#2.Program to print 1 to 20 numbers using the while loop
i = 1
while i <= 20:
    print(i)
    i += 1

#3.Program to equal operator and not equal operators
def equality_notequality(a, b):
    print("a == b:", a == b)
    print("a != b:", a != b)

equality_notequality(15,2)

#4.Program to print the odd and even numbers 
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

#5.Program to print largest number among three numbers
a = 10
b = 25
c = 15

if a > b and a > c:
    print("Largest number:", a)
elif b > a and b > c:
    print("Largest number:", b)
else:
    print("Largest number:", c)

#6. Program to print even number between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#7.Program to print 1 to 10 using the do-while loop statement
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

#8.Program to find Armstrong number or not 
num = 153  
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3  
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

#9.Program to find the prime or not
num = 29  
is_prime = True

if num > 1:
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

if is_prime and num > 1:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

#10.Program to find palindrome or not
n=input()
if n==n[::-1]:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is a palindrome")

#11.Program to check whether a number is EVEN or ODD using switch
num = 7  
match num % 2:
    case 0:
        print(num, "is Even")
    case 1:
        print(num, "is Odd")

#12.Print gender (Male/Female) program according to given M/F using switch
gender = 'M'  

match gender:
    case 'M':
        print("Male")
    case 'F':
        print("Female")
    case _:
        print("Invalid input")



