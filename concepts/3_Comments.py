# Comments

# Comments are notes for humans that Python ignores.
# They're like sticky notes in your code that explain what's happening.

# Help others understand your code
# Help future you remember what you did
# Document complex logic


# Single-line comments

# Printing Hello, world!
print("Hello, world!")  

# You can have multiple lines
# of comments by starting
# each line with a hash

age = 24  # Store user's age


# Multi-line comments

"""
This is a multi-line comment.
It can span several lines.
Great for longer explanations.
"""

def calculate_tip(bill):
    """
    Calculate 20% tip for a restaurant bill.
    Takes the bill amount and returns the tip.
    """
    return bill * 0.20

print("Tip for a $50 bill is:", calculate_tip(50))



subtotal = 100.00  # Store the subtotal of the bill
# Good: Explains why
# Using 1.0625 because sales tax in CA is 6.25%
total = subtotal * 1.0625

# Bad: States the obvious
# Multiply subtotal by 1.0625
total = subtotal * 1.0625


# Example
def new_method():
    # This method is the new way to process data
    pass
print("Starting process...")
# print("Debug info")  # Uncomment for debugging
new_method()
# old_method()  # Keeping for reference
