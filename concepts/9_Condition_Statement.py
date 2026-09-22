# Condition Statements are used to make decisions in a program based on whether a condition is True or False.

# Statement              Purpose                                  Example
# ---------------------------------------------------------------------------
# if                     Executes code when a condition is True    if age >= 18:
#
# if...else              Chooses between two possibilities       if age >= 18:
#                                                                  ...
#                                                                else:
#                                                                  ...
#
# if...elif...else       Checks multiple conditions               if age >= 18:
#                                                                  ...
#                                                                elif age >= 13:
#                                                                  ...
#                                                                else:
#                                                                  ...
#
# Nested if              An if statement inside another if       if age >= 18:
#                                                                  if has_id:
#                                                                      ...

# if Statement - Executes code when a condition is True
# they check if something is true or false, then act accordingly

# IF it’s raining THEN take umbrella
# IF battery < 20% THEN charge phone
# IF password correct THEN allow access

age = 18

if age >= 18:
    print("You can vote!")
    print("You're an adult")

# Check the condition (age >= 18)
# If True, run the indented code
# If False, skip it

# if-else statement
# Handle both True and False cases:

temperature = 25

if temperature > 30:
    print("It's hot")
else:
    print("Nice weather!")

# if-elif-else chains

score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up")
else:
    print("F - Need Improvement")

# Multiple Conditions
# Combine conditions with and, or, not:

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")

weekend = True
holiday = False
if weekend or holiday:
    print("No work today!")

raining = False
if not raining:
    print("Let's go outside!")

# Nested if statements
# Put if statements inside other if statements

has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")



# Common Mistakes

# Forgetting the colon
# Wrong
# if x > 5
#     print("Big")

# Right
# if x > 5:
#     print("Big")

# Using = instead of ==
# Wrong (assignment)
# if x = 5:
#     print("Five")

# Right (comparison)
# if x == 5:
#     print("Five")

# Wrong indentation
# Wrong
# if True:
# print("Hello")  # IndentationError

# # Right
# if True:
#     print("Hello")

bill = 3000

if bill >= 1000:
    print("5 percent discount")
elif bill >= 3000:
    print("10 percent discount")
elif bill >= 5000:
    print("20 percent discount")
else:
    print("No discount")

 # 5 percent discount