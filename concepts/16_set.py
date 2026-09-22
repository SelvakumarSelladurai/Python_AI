 

# A set is an unordered, mutable collection of unique elements

numbers = {10, 20, 20, 30, 30, 40}

# A set does not allow duplicate elements.

print(numbers)

# Property	        Set
# Ordered          	No
# Mutable	            Yes
# Duplicate values	No
# Indexing	        No
# Slicing	            No
# Different data types	Yes
# Syntax             	{}
# Main purpose	Unique values / membership

skills = {"Python", "React", "FastAPI"}

names = set()

# print(skills[0])  # TypeError: 'set' object is not subscriptable

empty = {}

empty2 = set()

print(type(empty))   # <class 'dict'>
print(type(empty2))  # <class 'set'>