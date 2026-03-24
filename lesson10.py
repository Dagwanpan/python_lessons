# Python Operators
# print(10 +5)

# sum1 = 100 + 50
# sum2 = sum1 + 250
# sum3 = sum2 + sum2

# =================
# Python Arithmetic operators
x = 15
y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)

# Division in Python
x = 12
y = 5

# Divison always returns a float:
# print(x / y)

# Floor division always returns an integer
# print(x // y)

# ========================
# Python assignment operators
# The walrus operator
# numbers = [1, 2, 3, 4, 5]

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")

# ================================
# Comparison operators
y = 5
y = 3

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

# Chaining comparison operators
x = 5
# print(1 < x < 10)

# print(1 < x and x < 10)

# ===========================
# Logical operators
x = 5
# print(x > 0 and x < 10)

# print(x < 5 or x > 10)

# print(not(x > 3 and x < 10))

# =========================
# Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]

z = x
# print(x is z)
# print(x is y)
# print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

# print(x is not y)

# Different between is and ==
x = [1, 2, 3]
y = [1, 2, 3]

# print(x == y)
# print(x is y)

# ========================
# Membership operators
fruits = ["apple", "banana", "cherry"]
# print("banana"in fruits)
# print("pineapple"not in fruits)

# ========================
text = "Hello World"
# print("H" in text)
# print("hello" in text)
# print("z" not in text)

# ==========================
# print(6 & 3)
# print(6 | 3)
# print( 6 ^ 3)

# ========================
# Operator Precedence
# print((6 + 3) - (6 + 3))

# print(100 + 5 * 3)

# Left to right evaluation
# print(5 + 4 - 7 + 3)

# Challenge: Operators Basics
a = 15
b = 4
print(a % b)
print(a // b)
print( a ** b)
a += 10