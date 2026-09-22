# String 

# A string(str) is a built-in Python data type used to represent and store a sequence of characters, such as letters, numbers, spaces, and symbols

# A string is text enclosed inside quotes ("")

# Strings are Immutable
# Once a string object is created, its individual characters cannot be changed

# Double quotes
name = "Selvakumar"

print(type(name))  # <class 'str'>

# Single quotes
Organization_name = 'SLRK'

print(type(Organization_name))

# Multiple Line quotes
my_long_string = """
Strings are text - any characters inside quotes.
Python doesn’t care if you use single or double quotes, just be consistent.
"""

print(type(my_long_string))

# String are immutable
org_name = "Sky"
org_name[2] = "d"  #TypeError: 'str' object does not support item assignment

# Combining strings
first_name = "Selva"
last_name = "kumar"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)

# Repetition
stars = "*" * 15
print(stars)

message = "sk "
print(message * 3)   # sk sk sk 

# String length
print(len(full_name))  # 11

empty = ""
print(len(empty))  # 0

# Strings are sequences of Characters
language = "Python"

# P  y  t  h  o  n
# 0  1  2  3  4  5

print(language[0])  # P
print(language[3])  # h

# Negative Indexing
print(language[-1]) # n  

# String Slicing
print(language[0:4])  #Pyth - string[start:stop]
