
# BREAK, CONTINUE, AND PASS

# break → stop the loop
# continue → skip the current iteration
# pass → do nothing

# Operator / Keyword | Meaning
# -------------------|----------------------------------------
# break              | Completely stops the current loop
# continue           | Skips the current iteration and continues
# pass               | Does nothing; acts as a placeholder


# break - immediately terminates the loop
for i in range(1, 11):  # break with for loop
    if i == 5:
        break

    print(i)
# 1,2,3,4

# i == 5 When i becomes 5:
#   ↓
# break
#   ↓
# STOP LOOP

# break with while
i = 1
while i <= 10:
    if i == 5:
        break

    print("count :",i)
    i += 1


# Search for a user:
users = ["Selva","rani","latha","durai"]

for user in users:

    if user == "Selva":
        print("User found")
        break

# Continue - Skip the current iteration and moves to the next iteration

for i in range(1, 6):   # Start at 1, stop before 6.

    if i == 3:
        continue

    print(i)
# output : 1, 2, 4, 5 

# Print only odd numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue

    print(i)

# 1, 3, 5, 7, 9

# pass : Do nothing
# It is mainly used as a placeholder when Python requires a statement but you dont want to execute anything yet.

for i in range(5):
    if i == 3:
        pass

    print(i)
# 0, 1, 2, 3, 4