# Loop is used to execute a block of code repeatedly

"""
A Loop is a control flow statement that repeatedly executes a block of
code until a specified condition is no longer satisfied or all items in
an iterable have been processed.
"""

# Loop    | Used for                                      | Example
# --------|-----------------------------------------------|-------------------------
# for     | Iterate over a sequence/collection or range   | for i in range(5):
# while   | Repeat while a condition remains True         | while count < 5: 

# Without Loops
# print("Hello!")
# print("Hello!")
# print("Hello!")
# print("Hello!")
# print("Hello!")

# range() is extremely important with for loops.
for i in range(5):
    print(i)  # python is 0 indexing language
    print("Hello!")

# range(start, stop)
for i in range(1,6):
    print(i)
# Output: 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

for i in range(10,0,-2):
    print(i)
# Output: 10, 8, 6, 4, 2


# while Loop repeats as long as its condition is True.

# while condition:
count = 1

while count <= 5:
    print("count =>",count)
    count += 1

# Example 

password = ""

while password != "1234":
    password = input("Enter password: ")

print("Login successfully")

# Enter password: 12
# Enter password: 1234
# Login successfully



# FOR LOOP:
#   - Used when we know what we want to iterate over.
#   - Commonly used with range(), lists, strings, etc.
#   - Automatically moves to the next iteration.
#
# WHILE LOOP:
#   - Used when repetition depends on a condition.
#   - We must manually update the variable/condition.
#   - Continues running while the condition is True.