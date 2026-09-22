
# Data Structure is a method of organizing and storing data so that it can be used efficiently

name1 = "selva"
name2 = "Kumar"
name3 = "Selvakumar"
name4 = "Durai"
# This works, but becomes difficult if you have 1,000 names.

names = ["Selva", "Kumar", "Selvakumar", "Durai"]

print(names[0])


# Data Structure   Python Type   Example                  Main Purpose
# -------------------------------------------------------------------------
# List             list          [10, 20, 30]             Ordered, mutable collection
# Tuple            tuple         (10, 20, 30)             Ordered, immutable collection
# Set              set           {10, 20, 30}             Collection of unique values
# Dictionary       dict          {"name": "Arun"}         Key-value pairs
# String           str           "Python"                 Sequence of text characters


# Store data
#    ↓
# Search data
#    ↓
# Add data
#    ↓
# Remove data
#    ↓
# Update data
#    ↓
# Sort data
#    ↓
# Process data


numbers = [10, 50, 20, 30, 40]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
# 50

# Find the 2nd Largest Number
list1 = [10,43,53,64,36]

list1.sort()
print(list1)  # [10, 36, 43, 53, 64]

print(list1[-2])  # 53


# Data Structures
# │
# ├── Python Built-in
# │   ├── List
# │   ├── Tuple
# │   ├── Set
# │   ├── Dictionary
# │   └── String
# │
# ├── Linear Data Structures
# │   ├── Array
# │   ├── Stack
# │   ├── Queue
# │   └── Linked List
# │
# ├── Non-Linear Data Structures
# │   ├── Tree
# │   ├── Binary Tree
# │   ├── Binary Search Tree
# │   ├── Heap
# │   └── Graph
# │
# └── Advanced
#     ├── Hash Table
#     ├── Trie
#     └── Graph algorithms