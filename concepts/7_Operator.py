# Operator is a special symbol or Keyword in Python that performs an operation on one or more values (operands) and produces a result.

# Operators are used to perform operations on data.

# Operators
# │
# ├── 1. Arithmetic Operators
# ├── 2. Assignment Operators
# ├── 3. Comparison Operators
# ├── 4. Logical Operators
# ├── 5. Identity Operators
# ├── 6. Membership Operators
# └── 7. Bitwise Operators

# Arithmetic Operators 
# Used to perform mathematical operations

# Operator   Name             Example       Result      Code
# ----------------------------------------------------------------
#    +       Addition         10 + 5          15        print(a + b)
#    -       Subtraction      10 - 5           5        print(a - b)
#    *       Multiplication   10 * 5          50        print(a * b)
#    /       Division         10 / 5         2.0        print(a / b)
#-   //      Floor Division   10 // 3          3        print(a // 3)
#    %       Modulus          10 % 3           1        print(a % 3)
#    **      Exponentiation   2 ** 3           8        print(2 ** 3)


# Assignment Operators
# Used to assign or update values

# Operator | Example  | Same As       | Meaning
# ---------|----------|---------------|---------------------------
# =        | x = 5    | x = 5         | Assign value
# +=       | x += 3   | x = x + 3     | Add and assign
# -=       | x -= 3   | x = x - 3     | Subtract and assign
# *=       | x *= 3   | x = x * 3     | Multiply and assign
# /=       | x /= 3   | x = x / 3     | Divide and assign
# %=       | x %= 3   | x = x % 3     | Remainder and assign
#-//=      | x //= 3  | x = x // 3    | Floor divide and assign
# **=      | x **= 3  | x = x ** 3    | Power and assign
# &=       | x &= 3   | x = x & 3     | Bitwise AND and assign
# |=       | x |= 3   | x = x | 3     | Bitwise OR and assign
# ^=       | x ^= 3   | x = x ^ 3     | Bitwise XOR and assign
# >>=      | x >>= 3  | x = x >> 3    | Right shift and assign
# <<=      | x <<= 3  | x = x << 3    | Left shift and assign
# :=       | x := 3   | Assignment     | Assignment expression

number = 10
number += 5
print(number)  # 15

number -= 5
print(number)  # 12

price = 100
price *= 2
print(price)  # 200

marks = 100
marks /= 4
print(marks)  # 25

# Comparison Operators
# used to compare two values.
# The result of a comparison is always a Boolean value:
# True or False.
# Operator | Example    | Meaning
# ---------|------------|----------------------------
# ==       | x == y     | Equal to
#-!=       | x != y     | Not equal to
# >        | x > y      | Greater than
# <        | x < y      | Less than
# >=       | x >= y     | Greater than or equal to
# <=       | x <= y     | Less than or equal to

x = 10
y = 5

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= y)   # True
print(x <= y)   # False

# Logical operators
# used to combine or reverse conditions.
# They work with Boolean values (True / False) and return
# a Boolean result.

# Operator | Example              | Meaning
# ---------|----------------------|--------------------------------
# and      | x > 5 and y < 10     | True if BOTH conditions are True
# or       | x > 5 or y < 10      | True if AT LEAST ONE is True
# not      | not(x > 5)           | Reverses the Boolean result

number1 = 10
number2 = 5

print(number1 > 5 and number2 < 10)
# True and True -> True

print(number1 > 5 or number2 > 10)
# True
# True or False → True

print(not number1 > 5)
# False
# not True → False

#Membership operators
# used to check whether a value exists inside a collection or sequence.

# They return a Boolean value:
# True or False

# Operator | Example              | Meaning
# ---------|----------------------|--------------------------------
# in       | x in collection      | True if x exists in collection
# not in   | x not in collection  | True if x does NOT exist

# Membership with Strings
name = "Python"
print("Pyt" in name)  # True

# Membership with Tuple
language = ("Python", "JavaScript", "TypeScript")
print("JavaScript" in language)  # True
print("Java" in language)  # False

print(
    "Java" not in language)  # True

# Membership with Set
skills = {"Python", "React", "FastAPI"}
print("React" in skills)  # True

user = {
    "name": "Selva",
    "age": 24,
    "role": "Developer"
}

print("name" in user)  # True
print("Selva" in user)  # False
print("Selva" in user.values(), "Selva" in user.keys())  # True False



# Bitwise operators
# It work on the individual bits of integers.
#
# They operate at the binary (0 and 1) level.

# Operator | Example   | Meaning
# ---------|-----------|--------------------------------
# &        | x & y     | Bitwise AND
# |        | x | y     | Bitwise OR
# ^        | x ^ y     | Bitwise XOR
# ~        | ~x        | Bitwise NOT
# <<       | x << n    | Left shift
# >>       | x >> n    | Right shift


# Decimal    Binary
# -------    ------
# 0          0000
# 1          0001
# 2          0010
# 3          0011
# 4          0100
# 5          0101
# 6          0110
# 7          0111
# 8          1000

test1 = 5
test2 = 3

print(test1 & test2) # 1

test3 = 5

print(~test3)  # -6