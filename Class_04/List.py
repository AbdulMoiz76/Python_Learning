# List:
# A List is mutable (changeable) collection of items.

marks = [12,34,12,56,78,12,90,76]
print(marks)
print(type(marks))
print(marks[0]) # Accessing the first element
print(marks[1]) # Accessing the second element
print(marks[2]) # Accessing the third element
print(marks[3]) # Accessing the fourth element


# List Slicing:
student = ["Ali",97.7,"Lahore"]
print(student[0:2]) # Accessing the first two elements

# List Methods:


# append() - Adds an item to the end of the list
marks.append(100)
print(marks)

# insert() - Adds an item at a specified index
marks.insert(2,67)
print(marks)

# remove() - Removes the first occurrence of an item
marks.remove(56)
print(marks)

# pop() - Removes the item at a specified index
marks.pop(3)
print(marks)

# sort() - Sorts the list in ascending order
print(marks.sort())
print(marks)
print(marks.sort(reverse=True)) # Sorts the list in descending order
print(marks)

# reverse() - Reverses the order of the list
marks.reverse()
print(marks)

# count() - Returns the number of occurrences of an item
print(marks.count(12)) # Count the number of occurrences of 12

# index() - Returns the index of the first occurrence of an item
print(marks.index(12)) # Returns the index of the first occurrence of 12

# extend() - Adds the elements of a list (or any iterable) to the end of the current list
marks2 = [1,2,3]
marks.extend(marks2)
print(marks)

# clear() - Removes all items from the list

marks.clear()
print(marks) # Prints an empty list