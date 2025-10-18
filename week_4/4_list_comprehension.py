# What is list comprehension ? create a list using a loop
from curses.panel import update_panels


list1 = [1, 2, 3, 4, 5]

list1 = [(1, i, "IITM") for i in range(1, 6) if i % 2 == 0]
# [output  iteration/loop condition/filter]
print(list1)
list1 = [f"number : {i}" for i in range(1, 6) if i % 2 == 0]
print(list1)

list2 = [i for i in range(0, 101, 5)]
print(list2)

# mapping a list
list2 = ["apple", "mango", "dominoes"]
upper_fruit = [fruit.upper() for fruit in list2]
print(upper_fruit)
