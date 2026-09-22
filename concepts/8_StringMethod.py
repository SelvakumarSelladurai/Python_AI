# String manipulation

name = "Selvakumar"

# f is used to create an f-string (formatted string)
# This string contains expressions inside {} that should be evaluated and inserted into the string
string = f"Hi there, my name is {name}"

print(string)

hash = "#"
hashes = hash * 20
print(hashes)

# Python String Methods

# | Method          | Purpose                        | Example                                      | Result            |
# |-----------------|--------------------------------|----------------------------------------------|-------------------|
# | `.upper()`      | Convert to uppercase           | `"python".upper()`                           | `PYTHON`          |
# | `.lower()`      | Convert to lowercase           | `"PYTHON".lower()`                           | `python`          |
# | `.capitalize()` | Capitalize first character     | `"python".capitalize()`                      | `Python`          |
# | `.title()`      | Capitalize each word           | `"hello world".title()`                      | `Hello World`     |
# | `.swapcase()`   | Swap uppercase/lowercase       | `"PyThOn".swapcase()`                        | `pYtHoN`          |
# | `.strip()`      | Remove spaces from both ends   | `" Hello ".strip()`                          | `Hello`           |
# | `.lstrip()`     | Remove left-side spaces        | `" Hello".lstrip()`                          | `Hello`           |
# | `.rstrip()`     | Remove right-side spaces       | `"Hello ".rstrip()`                          | `Hello`           |
# | `.replace()`    | Replace text                   | `"I like Java".replace("Java", "Python")`    | `I like Python`   |
# | `.find()`       | Find position of text          | `"Python".find("th")`                        | `2`               |
# | `.index()`      | Find position of text          | `"Python".index("th")`                       | `2`               |
# | `.count()`      | Count occurrences              | `"banana".count("a")`                        | `3`               |
# | `.startswith()` | Check beginning                | `"Python".startswith("Py")`                  | `True`            |
# | `.endswith()`   | Check ending                   | `"Python".endswith("on")`                    | `True`            |
# | `.split()`      | Split into a list              | `"A,B,C".split(",")`                         | `['A', 'B', 'C']` |
# | `.join()`       | Join strings                   | `"-".join(["A", "B"])`                       | `A-B`             |
# | `.isdigit()`    | Check digits                   | `"123".isdigit()`                            | `True`            |
# | `.isalpha()`    | Check alphabetic characters   | `"Python".isalpha()`                         | `True`            |
# | `.isalnum()`    | Check letters/numbers          | `"Python123".isalnum()`                      | `True`            |
# | `.isspace()`    | Check whitespace               | `"   ".isspace()`                            | `True`            |
# | `.islower()`    | Check lowercase                | `"python".islower()`                         | `True`            |
# | `.isupper()`    | Check uppercase                | `"PYTHON".isupper()`                         | `True`            |
# | `.istitle()`    | Check title case               | `"Hello World".istitle()`                    | `True`            |


# Case Methods

text = "hello python"

print(text.upper())  # HELLO PYTHON
print(text.lower())  # hello python
print(text.capitalize()) # Hello python
print(text.title())  # Hello Python

# Removing Whitespace
text1 = "   Selvakumar   "

print(text1.strip())     # Selvakumar
print(text1.lstrip())    # Selvakumar
print(text1.rstrip())    #    Selvakumar

username = input("Enter username: ")

username = username.strip()
print(username)

# find() - Returns the index where the substring starts.

full_name = "Selva Kumar"

print(full_name.find("Selva"))   # 0 because the start index is 0

# count()
emp_name = "Selladurai"

print(emp_name.count("r"))   # 1

# startswith() and endswith()

filename = "report.pdf"

print(filename.startswith("report"))
# True
print(filename.endswith(".pdf"))
# True

# split()

language = "Python,JavaScript,React"
lang = language.split(",")

print(lang)

# join()

languages = ["Python", "JavaScript", "React"]
text = ", ".join(languages)

print(text)

# Checking Methods

# isdigit()
print("123".isdigit())  # true

# isalpha()
print("Python".isalpha())  # true

# isalnum()
print("Python123".isalnum())  # true


# STRING METHODS
# │
# ├── Change case
# │   ├── upper()
# │   ├── lower()
# │   ├── capitalize()
# │   └── title()
# │
# ├── Clean
# │   ├── strip()
# │   ├── lstrip()
# │   └── rstrip()
# │
# ├── Search
# │   ├── find()
# │   ├── index()
# │   └── count()
# │
# ├── Modify
# │   └── replace()
# │
# ├── Split / Combine
# │   ├── split()
# │   └── join()
# │
# └── Validate
#     ├── isdigit()
#     ├── isalpha()
#     ├── isalnum()
#     ├── isspace()
#     ├── islower()
#     └── isupper()