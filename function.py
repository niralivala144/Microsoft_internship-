# what is Function?
# A function is a block of code that runs only when it is called.

# why use Functions?

# 1. Avoid repeating code
# 2. Makes program clean and reuse
# 3. Easy to debug and reuse

# syntax:
# def function_name():
#ex:
def greet():
    print("Hello Students")
greet()

#-------------------------------------------------------------------
# Function with parameters
# Used to pass values

def greet(name):
    print(f"Hello {name}")
    greet()
    greet("shreyarth")
    greet("AICW")
    
#------------------------------------------------------------------
# Function with return Value
# Used when we want to send result back

def add(a,b):
    return a + b

result = add(2,3)
print(result)

#-----------------------------------------------------------------------------
# Task 1: create a function to calculate and return result.
# hint: use return statement
def calculate(a, b):
    return a * b + a - b
result = calculate(5, 3)
print(result)

# Task 2: create a function to check if a numbere is even and odd
#hint: use moduls operator(%)
num = int(input("Enter a number: "))
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(num))
print(result)

# Task 3: create a function to find the factorial of a number.
# hint: use a loop or recursion 
num = int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
result = factorial(num)
print(result)

#Task 4: create a function to find maximum of three numbers.
# hint: use if-else
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
result = find_max(A, B, C)
print(result)

# Task 5: create a function to check if a string is palindrome or not.
num = input("Enter a string: ")
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # remove spaces and convert to lowercase
    return s == s[::-1]  # check if string is equal to its reverse

if is_palindrome(num):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Task 6: create a function to calculate the area of a circle given its radius.
# hint : area = π * r^2(use 3.14 for π)
# radius= 5
#area = 3.14 * radius ** 2

def area_of_circle(radius):
    pi = 3.14
    return pi * radius ** 2

radius = int(input("Enter the radius of the circle: "))
print(area_of_circle(radius))