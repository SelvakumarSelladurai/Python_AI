
# Tuple is an ordered, immutable collection of elements that can store values of different data types and allows duplicate values

# A tuple is created using parentheses ().

numbers = (10, 20, 30, 40)

data = (10, "Python", 3.14, True)

print(data)   # (10, 'Python', 3.14, True)

# Empty
empty = ()

# Single Element Tuple
number = (10)  # This is not a tuple

print(type(number))   # <class 'int'>

number1 = (10,)

print(type(number1))   # <class 'tuple'>

# indexing 

fruits = ("Apple", "Banana", "Orange", "Mango")

print(fruits[0])
# Apple

print(fruits[2])
# Orange

print(fruits[-1])
# Mango


# Value      Apple    Banana    Orange    Mango
# Index        0        1          2        3
# Negative    -4       -3         -2       -1

# Slicing

number = (10, 20, 30, 40, 50)

print(number[1:4])  # (20, 30, 40)

print(numbers[:3])
# (10, 20, 30)

print(numbers[2:])
# (30, 40, 50)

print(numbers[::-1])
# (50, 40, 30, 20, 10)

# Tuple is Immutable - You cannot change an existing tuple element.

numb = (10, 20, 30)

# num[0] = 100 - TypeError
 
# Tuple Methods

# count() - counts how many times a value appears

n = (10, 20, 10, 30, 10)
print(n.count(10))  # 3

# index() - Finds the index of a value

print(n.index(30))  # 3


# Tuple Unpacking 
person = ("Selvakumar", 25, "Developer")

name, age, role = person

print(name)
print(age)
print(role)

# Nested Tuples

data = (
    ("Arun", 25),
    ("Kumar", 30),
    ("Raj", 28)
)

print(data[0])
# ('Arun', 25)

print(data[0][0])
# Arun