# LIST METHODS  IN PYTHON

# 1. append() - appends an element to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# 2. extend() - extends the list by appending all the items from the iterable
my_list.extend([5, 6])
print(my_list)

# 3. insert() - inserts an element at a specified position
my_list.insert(0, 0)
print(my_list)

# 4. remove() - removes the first item from the list that matches the specified value
my_list.remove(3)
print(my_list)

# 5. pop() - removes the item at the specified position in the list and returns it
popped_item = my_list.pop(2)
print(popped_item)
print(my_list)

# 6. clear() - removes all items from the list
my_list.clear()
print(my_list)

# 7. index() - returns the index of the first item that matches the specified value
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3))

# 8. count() - returns the number of times a specified value occurs in the list
print(my_list.count(2))

# 9. sort() - sorts the items of the list in place
my_list.sort()
print(my_list)

# 10. reverse() - reverses the elements of the list in place
my_list.reverse()
print(my_list)



