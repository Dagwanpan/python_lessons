# Python Tuples
thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# Allow Duplicate 
thistuple = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thistuple)

# Tuple Length
thistuple = ["apple", "banana", "cherry"]
# print(len(thistuple))

# Create tuple with one item "include a comma after the item"
thistuple = ("apple",)
# print(type(thistuple))

# Not a tuple
thistuple = ("apple")
# print(type(thistuple))

# Tuple items - data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

# type()
mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round brackets
# print(thistuple)

# =============================
# Python access tuple items
thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# Negative indexing
thistuple = ('apple', 'banana', 'cherry')
# print(thistuple[-1])

# Range of Indexes
# Return the third, fourth, and fitth items:
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
# print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":
# print(thistuple[:4])

# This example returns the items from "cherry" and to the end:
# print(thistuple[2:])

# Range of Negative indexes
# This example returns the items from index -4 (included) to index -1 (excluded)
# print(thistuple[-4:-1])

# Check if items exists
# Check if "apple" is present in the tuple:
thistuple = ('apple', 'banana', 'cherry')
# if 'apple' in thistuple:
#     print('Yes, "apple" is in the fruits tuple')

# ==================================================
# Python - Update Tuples
# Change tuple values
# Convert the tuple into a list to be able to change it:
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'

x = tuple(y)

# print(x)

# Add items
# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ('apple', 'banana', 'cherry')
y = list(thistuple)
y.append('orange')
thistuple = tuple(y)

# print(thistuple)

# Create a new tuple with the value "orange", and add that tuple:
thistuple = ('apple', 'banana', 'cherry')
y = ('orange',)
thistuple += y
# print(thistuple)

# Remove times
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ('apple', 'banana', 'cherry')
y = list(thistuple)
y.remove('apple')
thistuple = tuple(y)

# print(thistuple)

# The del keyword can delete the tuple completely:
thistuple = ('apple', 'banana', 'cherry')
del thistuple
#print(thistuple)    # This will raise an error because the tuple no longer exists


# ==========================================================
# Python Unpack Tuples

# Packing a tuple:
fruits = ('apple', 'banana', 'cherry')

# Unpacking a tuple:
fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# Using asterisk *
# Assign the rest of the values as a list called "red":
fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')

(green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

fruits = ('apple', 'mango', 'papaya', 'pineapple', 'cherry')
(green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# ===========================================================
# Python - Loop tuples
thistuple = ('apple', 'banana', 'cherry')
# for x in thistuple:
#     print(x)

# Print all items by referring to their index number:
thistuple = ('apple', 'banana', 'cherry')
# for i in range(len(thistuple)):
#     print(thistuple[i])

# Print all items, using a while loop to go through all the index numbers:
thistuple = ('apple', 'banana', 'cherry')
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i += 1

# ======================================================
# Python - Join Tuples
# Join two tuples:
tuple1 = ('a', 'b', 'c')

tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
# print(tuple3)

# Multiply Tuples
# Multiply the fruits tuple by 2:
fruits = ('apple', 'banana', 'cherry')
mytuple = fruits * 2
# print(mytuple)


# =================================
# Python - Tuple Methods
# count()
# index()

# Python Tuples Code Challenge
fruits = ('apple', 'banana', 'cherry')
print(fruits[1])
print(len(fruits))
(a, b, c) = fruits
print(b)