

"""
A function is a reusable block of code that performs a specific task.

Instead of writing the same code again and again, we put it inside a function and call it whenever we need it.

Why use functions?


Don’t repeat yourself: Write code once, use it many times
Stay organized: Break complex programs into smaller pieces
Fix bugs easier: Change code in one place, affects everywhere
Test your code: Test each function separately

"""

# without a function 

name = "Latha"
print("Hello", name)

name = "Selva"
print("Hello", name)

name = "durai"
print("Hello", name)

name = "Rani"
print("Hello", name)

# with a function

def greet(name):   # name : parameter
    print("Hello", name)

greet("Selva")   # Selva : argument
greet("Latha")
greet("Durai")
greet("Rani")

# Parameters let you pass data into functions

# def       → tells Python we are defining a function
# greet     → function name
# ()        → parameters go here
# :         → function body starts
# print()   → code executed when function is called


def detail(first_name, last_name):
    print(f"Hello, {first_name, last_name}")  

detail(first_name="Selva", last_name="Kumar")  # Hello, ('Selva', 'Kumar')
detail(last_name="Kumar", first_name="Selva")  # Hello, ('Selva', 'Kumar')


# Multiple Parameters

def add(a, b):
    print(a + b)

add(10, 20)  # 30
add(100, 50)  # 150

# intro example

def intro(name, age, city):
    print("Name:", name)
    print("Age:",age)
    print("City:",city)

    # pass

intro("Selva",25,"Amaravathinagar")

# return 

# using print

def add1(a, b):
    print(a + b)

# using return - Sends a value out of a function back to the code that called it
# Send a value back to the place where the function was called.

def sub(a, b):
    return a - b

result = add1(10, 20)
result2 = sub(20, 40)
print(result, result2)

print(result)


# Function with Return Value

def multiply(a, b):
    return a * b

result2 = multiply(5, 4)

print(result2)

# Multiple return Values

def calculate(a, b):
    return a + b, a -b

result3 = calculate(10, 5)
print(result3)

# Default Parameters

def greet(name = "Selva"):
    print("Hello", name)

greet()

# Keyword Arguments 

def introduce(name, age, city):
    print(name, age, city)

introduce("Latha", 25, "Tiruppur")  # Latha 25 Tiruppur

# Positional Arguments

def introduce(name, age):
    print(name, age)

introduce("Latha", 25)


# Functions with logic

def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather")

check_weather()   # Nice weather


# Common Mistakes

# 1. Forgetting parentheses when calling
# check_weather - This doesn't call the function
# check_weather() - parentheses are required

# 2. Forgetting the colon
# def greet()
    #  print("Hello")
# def greet():
#     print("Hello")

# # Wrong - not indented
# def greet():
# print("Hello")

# # Right - must indent function body
# def greet():
#     print("Hello")


# Example
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")  

calculate_total(100, 0.08, 10)   # Total: $98.0   # poitional arguments
calculate_total(price=100, tax_rate=0.08, discount=10)  # Total: $98.0  # Keyword arguments



# First and last number

def sample_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]

    return first_number, last_number

first, last = sample_function()
print(first)   # 1
print(last)    # 5

# min&max

def get_min_max(numbers):
    return min(numbers), max(numbers)

mininum, maximum = get_min_max([5, 2, 8, 1, 9])

print(f"Min: {mininum}, Max: {maximum}")  # Min: 1, Max: 9

result = get_min_max([10, 4, 8, 5, 9])
print(result)   # (4, 10)