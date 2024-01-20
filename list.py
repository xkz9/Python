# mylist = ["Leonardo's list", 9, 79, False]

# The apppend funtion adds whatever value you want to the end of your list.

# print (mylist)
# mylist.append("Hello")
# print(mylist)

# The remove function removes whatever is present in the brackets mylist.remove(xx)

# mylist.remove(False)
# print(mylist)

# The pop function is used to remove a particular value by using it's index. 

# mylist.pop(2)
# print(mylist)

# Th insert function adds a particular value at  a particular index in the list

# mylist.insert(2, 200)
# print(mylist)

# mylist.reverse()
# print(mylist)

# The clear function gives you an empty list when ran (removes all elements of the list). 

# mylist.clear()
# print(mylist)

# The .copy function makes a shallow copy of. A shallow copy mean both lists are stored differently in tyhe memory , but are referncing the same elements

# newlist = mylist.copy()
# print(newlist)

# sorting is done based on the alphabetical order based on letters 

# mylist = [5, 7, 254 ,  326, 34, 674, 26348579, 34, 67, 89, 7, 69]
# mylist.sort()
# mylist.sort(reverse = True)
# print(mylist)

# The sort function autimatically sorts in ascensing order, but when you write reverse = True it puts them in descending order.

# mylist = ["Hello", "Hello", "Bye", "GoodBye"]
# mylist.sort(reverse = True)
# print(mylist)

# Write a Python code to create a list of numbers from 1 to 10.
# Add the numbers 11 and 12 to the list.
# Remove the number 3 from the list.

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist.pop(2)
mylist.append(11)
mylist.append(12)
print(mylist)