# If else
"""
if (statement/condition):
    TODO
elif (statement): 
    TODO
else:
    TODO
"""

marks = 99

if marks > 90:
    print("S")
    if marks > 95:
        print("AWESOME")
elif marks >= 80 and marks < 90:    # if the previous if statement is not true
    print("A")
else:   # If none of the if statements are true.
    print("NOT S OR A")


# shorthand if else

num = 6

print(num) if (num == 10 or num == 5) else print("not 10 or 5")
