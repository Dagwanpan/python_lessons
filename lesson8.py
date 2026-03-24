# Python Strings
# print("Hello")
# print('Hello')

# Quotes inside quotes
# print("It's a alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

# Assign String to a Variable
a = "Hello"
#print(a)

# Multiline Strings
a = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, send do eiusmod tempor incididunt ut labore et dolore magna aligua."""
# print(a)
a = '''
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua.'''
# print(a)

# Strings are Arrays
a = "Hello, World!"
# print(a[1])

# Looping through a string
#for x in "banana":
    # print(x)

# String Length
a = "Hello, World!"
# print(len(a))

# Checking string
# Check if "free"is present in the following text:
txt = "The best things in life are free!"
# print("free" in txt)

txt = "The best things in life are free!"
#if "free" in txt:
    # print("Yes 'free' is present.")


# Check if NOT
txt = "The best things in life are free!"
# print("expensive" not in txt)

txt = "The best things in life are free!"
#if "expensive" not in txt:
    #print("No, 'expensive' is NOT present")

# ==========================
# Python slicing strings
b = "Hello, World!"
# print(b[2:5])

# Slice from the Start
b = "Hello, World!"
# print(b[:5])

# Slice to the end
b = "Hello, World!"
# print(b[2:])

# Negative indexing
b = "Hello, World!"
# print(b[-5:-2])

txt = "Hello World"
x = txt[2:5]
# print(x)

# Python Modify Strings
# Upper case
a = "Hello, World!"
# print(a.upper()) 

# Lower case
a = "Hello, World!"
# print(a.lower())

# Remove white space
a = " Hello, World! "
# print(a.strip())

# Replace string
a = "Hello, World!"
# print(a.replace("H", "J"))

# Split string
a = "Hello, World!"
# print(a.split(",")) # Return ['Hello', 'World']

# ==================================
# String concatenation
a = "Hello " 
b = "World"
c = a + b
# print(c)

a = "Hello"
b = "World"
c = a + " " + b
# print(c)

# ===========================
# Python Format - Strings
age = 36
# This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)

# F-Strings
age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# Place holders and modifiers
price = 59
# txt = f"The price is {price} dollars"
# print(txt)

price = 59
# txt = f"The price is {price:.2f} dollors"
# print(txt)

# txt = f"The price is {20 * 59} dollars"
# print(txt)

# Error
# txt = "We are the socalled "Vikings" from the north." 

# Correct!
# txt = "We are the so-called \"vikings\" from the north."
# print(txt)

# ==========================
# Python String Methods
# ===============================
# Exercise
txt = "Hello, World!"
print(txt[2:5])
print(txt.upper())

name = "Python"
print(f"I love {name}")