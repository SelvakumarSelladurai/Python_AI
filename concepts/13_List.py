
# List is an ordered, mutable collection of elements that can store values of different data types and allows duplicate values.

# It is used to store multiple values in a single variable.

my_list = []

numbers = [10, 20, 30, 40, 50]

age = 24
has_licence = True

different_datatype = ["Selva", 25, age, True, has_licence]

# Indexing - zero-based indexing

names = ["Selva", "Kumar", "Selvakumar", "SK"]

# Value     Selva    Kumar    Selvakumar  SK
# Index       0        1          2        3
# Negative   -4       -3         -2       -1

print(names[1]) # Kumar

print(names[3]) # SK

print(names[-2]) # Selvakumar

# Changing List Element 
names[2] = "Latha"

print(names)   # ['Selva', 'Kumar', 'Latha', 'SK']

# Adding Elements

# append()

names.append("Selladurai")
print("append :",names)  # ['Selva', 'Kumar', 'Latha', 'SK', 'Selladurai']

# insert()

names.insert(1, "rani")
print("insert ",names)  # ['Selva', 'rani', 'Kumar', 'Latha', 'SK', 'Selladurai']

# remove() - Removes a specific value
names.remove("Selva")

print("Remove :",names)

names.append("Vijay")
# pop() - Removes an element using its index and return it.

last = names.pop()
print("last",last)  # Vijay

# Adding Multiple Elements
# extend()

name1 = ["Selva", "Rani"]
name1.extend(["latha", "durai"])

print("extend",name1)  # ['Selva', 'Rani', 'latha', 'durai']


# clear() - Remove everything

fruits = ["Apple", "Banana", "Orange"]

fruits.clear()

print(fruits)   # []

# index - find the position

fruit1 = ["Apple", "Banana", "Orange"]

print(fruit1.index("Banana"))  # 1

# List Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40]

# start → included
# stop  → excluded

print(numbers[:3])   # [10, 20, 30]
print(numbers[2:])   # [30, 40, 50]
print(numbers[::-1]) # [50, 40, 30, 20, 10]


# Searching in a List

# in or not in 

fruits = ["Apple", "Banana", "Orange"]

print("Apple" in fruits)
# True

print("Mango" in fruits)
# False

print("Mango" not in fruits)
# True


family_name = ["Selladurai", "Latha", "Selvarani", "Selvakumar"]

for i in range(len(family_name)):
    print(i + 1, family_name[i])

# 1 Selladurai
# 2 Latha
# 3 Selvarani
# 4 Selvakumar


# Sorting 

number1 = [50, 10, 40, 20, 30]

# number1.sort()

# print(number1)  # [10, 20, 30, 40, 50]

number1.sort(reverse=True)

print(number1)  # [50, 40, 30, 20, 10]


# Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]