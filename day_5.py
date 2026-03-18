# check wether a character is a vowel or consonant
char = input("Enter a character: ")
if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

# crate a simple calculator  using if-elif.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

print("Result:", result)

# ---------------------------------------------------------
# bank account 

# initial bal: 10000

# choice
# a. Deposit
# b. Withdraw
# c. Check Balance

# deposit = 1000

# balance = balance + 1000
# print(balance)

# main balance = 11000

# withdraw = 5000
# balance = balance - 5000
# print(balance)
# main balance = 6000

balance = 10000

print("A. Deposit")
print("B. Withdraw")
print("C. Check Balance")

choice1 = input("Enter your first choice: ")

if choice1 == "A":
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Balance now:", balance)

elif choice1 == "B":
    amount = int(input("Enter withdraw amount: "))
    balance = balance - amount
    print("Balance now:", balance)

elif choice1 == "C":
    print("Balance:", balance)


print("\nChoose another option")

print("A. Deposit")
print("B. Withdraw")
print("C. Check Balance")

choice2 = input("Enter your second choice: ")

if choice2 == "A":
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Balance now:", balance)

elif choice2 == "B":
    amount = int(input("Enter withdraw amount: "))
    balance = balance - amount
    print("Balance now:", balance)

elif choice2 == "C":
    print("Balance:", balance)
