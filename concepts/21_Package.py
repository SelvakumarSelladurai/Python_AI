
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

# Install a package
# pip install requests

# Install Specific version
# pip install requests=2.28.0

# Install multiple packages
# pip install pandas numpy matplotLib


# Creating requirements.txt

# pip freeze > requirements.txt

# This creates a file like:
# asttokens==3.0.2
# certifi==2026.7.22
# charset-normalizer==3.5.1
# colorama==0.4.6
# comm==0.2.3


# Installing from requirements.txt
# pip install -r requirement.txt

# Finding package 
# Pypi - https://pypi.org/
# Awesome Python - Curated list 

# Mistakes 

# Wrong - Package not installed or venv not activated
# import pandas 

# Name Conflicts
# import datatime
# datatime = "2024-01-01"  Now module is gone!

# Use different names
# import datetime
# date_string = "2024-01-01"
