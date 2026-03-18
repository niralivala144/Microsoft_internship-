# STRING METHODS IN PYTHON

# 1. upper() - Converts a string to uppercase
text = "hello world"
print(text.upper())

# 2. lower() - Converts a string to lowercase
print(text.lower())

# 3. title() - Converts the first character of each word to uppercase
print(text.title())

# 4. strip() - Removes leading and trailing whitespace
text_with_spaces = "   hello world   "
print(text_with_spaces.strip())

# 5. replace() - Replaces a specified phrase with another specified phrase
print(text.replace("world", "Python"))

# 6. split() - Splits a string into a list where each word is a list item
print(text.split())

# 7. join() - Joins the elements of an iterable to the end of the string
words = ["Hello", "World"]
print(" ".join(words))

# 8. find() - Searches the string for a specified value and returns the position of where it was found
print(text.find("world"))

# 9. count() - Returns the number of times a specified value occurs in a string
print(text.count("o"))

# 10. isalpha() - Returns True if all characters in the string are alphabetic
print(text.isalpha())

# 11. isdigit() - Returns True if all characters in the string are digits
number = "12345"
print(number.isdigit())

# 12. isspace() - Returns True if all characters in the string are whitespace
whitespace = "   "
print(whitespace.isspace())

# 13. startswith() - Returns True if the string starts with the specified value
print(text.startswith("hello"))

# 14. endswith() - Returns True if the string ends with the specified value
print(text.endswith("world"))

# 15. capitalize() - Converts the first character of a string to uppercase and the rest to lowercase
print(text.capitalize())

#16. swapcase() - Swaps the case of each character in the string
print(text.swapcase())

#17. len() - Returns the length of a string
print(len(text))

#18. strip() - Removes leading and trailing whitespace
print(text_with_spaces.strip())

#19. lstrip() - Removes leading whitespace
print(text_with_spaces.lstrip())

#20. rstrip() - Removes trailing whitespace
print(text_with_spaces.rstrip())


