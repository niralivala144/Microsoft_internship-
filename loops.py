# what is loop?
# A loop is used to repeat a block of code mutiple times until a certain condition is met.

# types of loops in python
# 1. for loop
# For variable in squence:
#   code block

# range(start, stop, step)
# 1. start (inclusive) 
# 2. stop (exclusive)
# 3. step (optional, default is 1)

for i in range(1, 6):
     print(i)
# key points:
 # 1. range(start, stop) generates numbers.
 # 2. loop runs fixed number of times.
 
#----------------------------------------------------------

# 2. while loop
# used when we repeat until a condition becomes false.
# while condition:
#   code block

i = 1
while i <= 5:
    print(i)
    i += 1
# key points:
# 1. while loop runs until the condition becomes false.
# 2. it is possible to create an infinite loop if the condition never becomes false.


#----------------------------------------------------------
# loop control statements
# 1. break: used to exit the loop immediately.

for i in range(1, 6):
    if i == 3:
        break
    print(i)
    
# 2. continue: used to skip the current iteration and move to the next iteration.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
# 3. pass: does nothing and serves as a placeholder
# for i in range(5):
for i in range(5):
    pass  # this is a placeholder for future code

#----------------------------------------------------------
# Task 1: print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i, end=' ')
    
# Task 2: print even numbers from 1 to 20 using a for loop.
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=' ')
        
#for i in range(2, 21, 2):
        # print(i, end=' ')
    
# Task 3: print odd numbers from 1 to 15 using a for loop.
for i in range(1, 16):
    if i % 2 != 0:
        print(i, end=' ')
        
#  for i in range(1, 16, 2):
   # print(i, end=' ')
    
# Task 4: print each character of the string "Python" using a for loop.
text = "Python"
for char in text:
    print(char)
    
# Task 5: print  all items in list.
data = ["data", "science", "AI"]
for item in data:
    print(item)
    
# Task 6: find the sum of numbers from 1 to 10 using a for loop.
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# Task 7: print multiplication table of 5 using a for loop.
num = 5
for i in range(1, 11):
    print(f"5 x {i} = {num * i}")
  
  # Task 8: count how many vowels are in string "Hello World" using a for loop.
text = "Hello World"
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in text:
    if char.lower() in vowels:
        count += 1
print("Number of vowels:",count)

# Task 9: print numbers in reverse order from 10 to 1 using a for loop.
for i in range(10, 0, -1):
    print(i, end=' ')
    
# Task 10: print square of numbers from 1 to 5 using a for loop.
for i in range(1, 6):
    print(f"{i}^2 = {i**2}")
   
    