
"""
A Dictionary is a mutable collection of key-value pairs used to
Store and Retrieve data using unique keys and Duplicates Not Allowed.

Think of them like a real dictionary where you look up a word (key) to find its definition (value).
"""

# Empty dictionary
my_dict = {}

user = {
    "name": "Selvakumar",
    "age": 25,
    "role": "Developer"
}

# Each key is associated with a value.
# "name"  → "Selvakumar"
# "age"   → 25
# "role"  → "Developer"
  
print(user)   # {'name': 'Selvakumar', 'age': 25, 'role': 'Developer'}

print(user["name"])  # Selvakumar
print(user["age"])  # 25

# get()

print(user.get("name"))   # Selvakumar

# print(user["email"])  # KeyError: 'email'

print(user.get("email"))  # None

print(user.get("email","Not Provided"))   # Not Provided

# Adding a New Key & Update 

user["role"] = "AI Engineer"

print(user)   # {'name': 'Selvakumar', 'age': 25, 'role': 'AI Engineer'}

# Removing Data - pop

user.pop("age")
print(user)  # 'name': 'Selvakumar', 'role': 'AI Engineer'}


# del 

del user["role"]
print(user)  # {'name': 'Selvakumar'}


# popitem() - Removes the last inserted key-value pair
user2 = {
    "name": "Ramesh",
    "age": 25
}

user2.popitem()

print(user2)  # {'name': 'Ramesh'}


# clear() - Removes everything


user2.clear()

print(user)

# keys()

user3 = {
    "name": "Selvarani",
    "age": 25,
    "role": "Teacher"
}

print(user3.keys()) # dict_keys(['name', 'age', 'role'])

print(user3.values()) # dict_values(['Selvarani', 25, 'Teacher'])

print(user3.items())  # dict_items([('name', 'Selvarani'), ('age', 25), ('role', 'Teacher')])

