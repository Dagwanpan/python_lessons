# Python List
thislist = ["apple", "banana", "cherry"]
# print(thislist)

# Allow Duplicate
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# List length
thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# Kust utens - Data Types
# String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [ 1, 5, 7, 9, 3]
list3 = [True, False, False, True]

mixlist = ["abc", 34, True, 40, "male"]

# Tyep
mylist = ["apple", "banana", "cherry"]
#print(type(mylist))

# List() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(type(thislist))
# print(thislist)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[2:5])

# =============================
# Python Access List Items
thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

thislist = ["apple", "banana", "cherry"]
# print(thislist[5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[2:])

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mongo"]
#print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list")

# ==========================
# Python Change list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
# print(thislist)

# Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["balckcurrant", "watermelon"]
# print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
# print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
# print(thislist)

mylist = ["apple", "banana", "cherry"]
mylist[0] = "kiwi"
# print(mylist[1])

# ================================
# Python - Add list items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
#print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
#print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
# print(thislist)

# =================== 
# Add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
# print(thislist)


# ==============================
# Python Remove list items
# Remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
# print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
# print(thislist)

# Remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop()
# print(thislist)

thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)

# Clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
# print(thislist)

# Python loop lists
thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# Loop through the index numbers
thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# Using a while loop
thislist = ["apple", "banana", "cherry"]

# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1

# Looping Using list comprehension
thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# ==============================
# Python list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", 'mango']

# newlist = []

# for x in fruits:
#     if "a"in x:
#         newlist.append(x)
        
# print(newlist)

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a"in x]

# print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]

# Conditions
# newlist = [x for x in fruits if x != "apple"]
# print(newlist)

# Condition is optional
# newlist = [x for x in fruits]
# print(newlist)

# Iterable
newlist = [x for x in range(10)]
# print(newlist)

newlist = [x for x in range(10) if x < 5]
# print(newlist)

# Expression
newlist = [x.upper() for x in fruits]
# print(newlist)

newlist = ["hello" for x in fruits]
# print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x if x != "banana" else "orange"for x in fruits]
# print(newlist)

# ==============================
# Python Sort lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
# print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
# print(thislist)

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
# print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
# print(thislist)

# Customize Sort Function
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
# print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
# print(thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
# print(thislist)

# ================================
# Python copy lists
# Use copay method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
# print(mylist)

# Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
# print(mylist)

# Use the slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
# print(mylist)

# ===================================
# Python Join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
# print(list3)
# for x in list2:
#     list1.append(x)
    
# print(list1)

list1.extend(list2)
# print(list1)

# ==================================
# python list methods

# List exercise

# Python Lists Code Challenge
colors = ["red", "greed", "blue"]
print(colors[0])

colors[1] = "yellow"
print(colors)

colors.append("purple")
print(colors)

colors.remove("red")
print(colors)