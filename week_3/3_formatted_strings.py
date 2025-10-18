# formatted outputs

name = "IITM"
year = 2025

sentence = f"Hello from {name}. This is {year}."
print(type(sentence))


# rounding in fstrings
value = 12.5678
print(f"{value:10.2f}")
print(f"     {round(value, 2)}")

# end parameter for print
print("Hello world", end="\n")

list1 = [1, 2, 3, 4, 5]
print(*list1, end="\n")  # unpacking

# what if i want to print a list in different lines without a loop
print(*list1, sep="\n")
print(*list1, sep="-")
