# Task 1: Covert the given string into a list of characters.
Text = "Hello,World!"
my_list = list(Text)
rs1 = Text.split(',')
print(my_list)
print(rs1)

# Task 2: Covert the given sentence into a list of words.
Text = "Hello, World! Welcome to Python programming."
my_list = list(Text)
rs2 = Text.split()
print(my_list)
print(rs2)

# Task 3: # Convert the given list into a single string.
my_list = ['H', 'e', 'l', 'l', 'o']
Text = ''.join(my_list)
print(Text)

# Task 4: Count the number of vowels in the given word using string and list methods only.
word = "education"
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
print(vowel_count)  # show the computed count

# Task 5: Count the frequency of the word "python" in the given string.
text = "python is easy and python is powerful."
x = text.count("python")
print(x)

# Task 6: Convert all names into Title Case using list methods.
names = ["john doe", "jane smith", "alice johnson"]
# convert each name to title case
result = [name.title() for name in names]
print(result)

# Task 7: Create a list with 4 elements, replace the second element, and convert the final list into a string.
lst = ["data", "science", "is", "fun"]
lst[1] = "Analytics"
final_string = ', '.join(lst)
print(final_string)

# Task 8: Replace the word "Java" with "Python" and print the output as a string.
text = "I love Java."
updated_text = text.replace("Java", "Python")
print(updated_text)

# Task 9: Join the list elements using a comma ( , ) and print as a string.
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
text = ", ".join(cities)
print(text)

# Task 10: Write a Python program to reverse the given string by:
text = "python"

# a. Converting the string into a list
x = list(text)
# b. Reversing the list
x.reverse()
# c. Converting the list back into a string
result = "".join(x)
print(result)

# Task 11: Write a Python program to replace the first and last words in the given string by:
text = "python is hard"
# a. Converting the string into a list
text = text.replace("python", "java")
text = text.replace("hard", "easy")
# b. Reversing the list
letter = list(text)
letter.reverse()
# c. Converting the list back into a string
result = ''.join(letter)
print(result)

