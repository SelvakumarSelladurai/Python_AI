
# Scope is a specific region of a program where a variable is visible and accessible.

# LEGB rule, which stands for Local, Enclosing, Global, and Built-in.

#   [ L ] Local       -> Inside the current function
#     [ E ] Enclosing   -> Inside outer nesting functions
#       [ G ] Global      -> At the top level of the script/module
#         [ B ] Built-in    -> Pre-defined Python names

# Scope = Where is this variable visible/accessible?


# Local Scope

# A variable created inside a function is normally a local variable.

def greet():
    name = "Latha"
    print(name)

greet()  # Latha

# def greet():
#     name = "Latha"


# greet()

# print(name)   # NameError: name 'name' is not defined
# This gives an error because name belongs to the function's local scope.

# name
#  ↓
# exists inside greet()
#  ↓
# local scope


name = "Selva"

def greet1():
    print(name)

greet1()  # Selva



# Local vs Global 

x = 100


def test():
    x = 50
    y = 30
    print(x)   # 50
    print(x + y)  # 80


test()

print(x)   # 100
# print(y)   # NameError: name 'y' is not defined