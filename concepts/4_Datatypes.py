# Data Type

"""
A data type is a classification that defines what kind of value an object can represent,
how that value is stored and handled and what operations can be performed on it.
"""

# In Python, every value is an object, and every object has a type.

"""
Numeric -- (int, float, complex)
String -- (string)
Sequence -- (list, tuple, range)
Binary -- (bytes, bytearray, memoryview)
Mapping -- (dict)
Boolean -- (bool)
Set -- (set, frozenset)
"""

# Numeric Types

# Integer - Whole numbers, positive or negative, without decimals, of unlimited length.
age = 25
score = -10
print(type(age)) # Output: <class 'int'>
print(type(score)) # Output: <class 'int'>

# Float - Numbers, positive or negative, containing one or more decimals.
price = 19.99
temperature = -5.5
print(type(price)) # Output: <class 'float'>
print(type(temperature)) # Output: <class 'float'>

# Complex - Numbers, positive or negative, containing a real and imaginary part is written using j.
# a + bj
z = 2 + 3j
print(type(z)) # Output: <class 'complex'>
print(z.real) # Output: 2.0
print(z.imag) # Output: 3.0

# Basic math operations
total = 10 + 5  # Addition
difference = 10 - 5  # Subtraction
product = 10 * 5  # Multiplication
quotient = 10 / 5  # Division
square = 10 ** 2  # Exponentiation / power
cubed = 2 ** 3 # Cubed


# Integer vs float division

result1 = 7 / 2  # Float division
print(result1)  # Output: 3.5
result2 = 7 // 2  # Integer division (floor division)
print(result2)  # Output: 3

# Can't use commas in numbers

million = 1,000,000  # This is a tuple, not a number
print(million)  # Output: (1, 0, 0)

million_number = 1000000  # Hard to read
million_number_readable = 1_000_000  # Readable and valid
print(million_number_readable)  # Output: 1000000

