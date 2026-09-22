# print("Hello world!")
# print("I am learning Python programming!")

# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)


# Store information
age = 24
name = "Selvakumar"
print("My name is", name, "and I am", age, "years old.")

# Make decisions
# if it's raining:
#     print("It's raining. Don't forget to take an umbrella!")
# else:
#     print("It's not raining. Enjoy your day!")

if age >= 18:
    print("You are an adult.")
else: 
    print("You are a minor.")

# repeat actions
# repeat 10 times:
#     do pushup

for i in range(5):
    print("This is repetition number", i + 1)

# Calculation things
# total = price + tax
total = 10 + 5
print("The total is:", total)


# Syntax - Every programming language has its own rules
# It's like grammar in human languages 

temperature = 35
# Python - clean and readable syntax
if temperature > 30:
    print("It's hot outside.")
    print("Turn on the AC")

# Other programming languages - like JavaScript
# if (temperature > 30) {
#     console.log("It's hot outside.");
#     console.log("Turn on the AC");
# }

Score = 86
# Indentation - Python uses indentation to define blocks of code
if Score >= 90:
    print("You got an A grade.")
    if Score >= 100:
        print("Perfect score!")

# Wrong indentation - will cause an error
# if Score >= 90:
#   print("You got an A grade.")  2 space instead of 4 space indentation
#    if Score >= 100:             4 space indentation
#      print("Perfect score!")    6 space indentation

# PEP8 - Python Enhancement Proposal 8 - syntax rules that make code run.
# Using 4 spaces for indentation, not tabs
# Limiting lines to 79 characters
# Naming conventions (like user_name instead of userName)

# Spacing - Python uses whitespace to separate code elements
x = 1 + 2
numbers = [1, 2, 3, 4, 5]

# Bad spacing - will cause an error
# x=1+2
# numbers=[1,2,3,4,5]

# Line length - Python limits lines to 79 characters for readability
long_string = (
    "This is a very long string that "
    "spans multiple lines for readability"
)
print(long_string)

# long_string = "This is a very long string that spans multiple lines for readability"
