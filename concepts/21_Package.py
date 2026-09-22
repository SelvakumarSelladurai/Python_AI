
# Python package is a directory used to organize related python modules and subpackage into a structured project.

# Package
#    ↓
# Folder
#    ↓
# Multiple Python modules
#    ↓
# Related functionality

# calculator/
# │
# ├── addition.py
# ├── subtraction.py
# ├── multiplication.py
# └── division.py

# calculator can be used as a package containing several modules


# my_project/
# │
# ├── main.py
# │
# └── calculator/
#     ├── __init__.py
#     ├── addition.py
#     └── subtraction.py

# my_project/
#     ↓
# project

# calculator/
#     ↓
# package

# addition.py
#     ↓
# module

# subtraction.py
#     ↓
# module

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# from calculator.addition import add
# from calculator.subtraction import subtract

# print(add(10, 5))
# print(subtract(10, 5))


# python has packages for everything:

# Web Scraping : Extract data from websites
# Data analysis : Process spreadsheets and databases
# AI/ML : Build intelligent applications
# APIs : Connect to online services
# Automation: Control your computer

# Using Packages
# Build in : Come with Python (no installation needed)
# External : Need to install first with pip


# Module: A single Python file (like math.py)
# Package: A folder containing multiple modules
# Function: A reusable block of code (like print() or sqrt())
# Class: A blueprint for creating objects

 