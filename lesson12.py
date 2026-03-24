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
print(thistuple[1])