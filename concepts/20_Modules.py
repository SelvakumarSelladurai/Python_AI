# module is simply a file containing Python Code (with a .py extension)

# Types of Modules
# 1. Built-in / Standard Library Modules - pre-installed with Python
# 2. User-defined Modules - Custom files you create yourself to organize ypur specific project code.
# 3. Third-party Modules - Package written by external developers ( like pandas or requests ) - install usng a package manager like pip ( )

# pip - Package Installer for Python

""" 
module is simply a Python file (.py) containing Python code such as:

variables
functions
classes
constants

example : math_utils.py
"""

# Creating Your Own Module
# project/
# │
# ├── calculator.py
# └── main.py

# calculator.py
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

# Importing a Module
import calculator

result = calculator.add(10, 20)

print(result)

# import math
# import random
# import datetime
# import sys

# number = random.randint(1, 100)
# now = datetime.datetime.now()

# print(math.sqrt(25))   # 5.0
# print(number)  # 73
# print(now)   # 2026-09-22 08:27:31.743302
# print(sys.version)   # 3.13.15 (tags/v3.13.15:4061bc4, Aug  5 2026, 13:05:39) [MSC v.1944 64 bit (AMD64)]
