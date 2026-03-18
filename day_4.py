# operators methods
# arithmetic operators
a = 10
b = 5
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50
print(a / b)  # Output: 2.0
print(a % b)  # Output: 0
print(a ** b) # Output: 100000

# Task 1: logical operators
a = 4
b = 5
c = 6
# Logical AND
print(b>a and c>b)  # Output: True

# Logical OR
print(b>a or c<b)   # Output: True

# Logical NOT
print(not (b>a))    # Output: False

# Task 2: assignment operators
x = +10
x += 10
print(x)  # Output: 20

y = -5
print(y)  # Output: -5

# Task 3: input: need user side input
num1 = input("Enter your num1 value: ")
num2 = input("Enter your num2 value: ")
print(int(num1) + int(num2))  

# if else condition
# => based on the condition if we have mutiples
# login with username and password
username = "nirali"
password = "12345"

if username == "nirali" and password == "12345":
    print("Login successful!")
else:
    print("Invalid username or password.")

# login with username and password
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "nirali" and password == "12345":
    print("Login successful!")
else:
    print("Invalid username or password.")
    
# check weather a number is positive, negative or zero
num = -5
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
# check if a number is even or odd
num = float(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# check weather a person is eligible to vote or not
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# find the largest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

# check weather a number is divisible by 5 or not
num = float(input("Enter a number: "))
if num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

# assign grade based on marks
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")

# check if a year is a leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# check wether a number is divisible by both 3 and 5
num = float(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is a multiple of both 3 and 5.")
else:
    print("The number is not a multiple of both 3 and 5.")
    