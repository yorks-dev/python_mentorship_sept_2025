"""
Write a Python program that takes a string as input and prints all the unique characters
in order of their frequency (from highest to lowest).
If two characters have the same frequency, they should appear in the order they first appeared
in the string.
"""

text = input("Enter a string : ")

# get rid of the spaces
text = text.replace(" ", "")

counted = ""  # empty string. we will populate it as we go on
char_count = {}

for ch in text:  # a

    if ch in counted:
        continue

    # countr the occurances
    count = 0
    for c in text:  # going through loop again to count the how many times
        if c == ch:
            count += 1

    char_count[ch] = count
    counted += ch

sorted_char_count = sorted(char_count.items(), key=lambda x: -x[1])
print(dict(sorted_char_count))
# abbbacba, counted = ""
# a : 3
