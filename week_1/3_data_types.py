# 1. Strings

import array
from math import pi
from operator import truth
from xml.sax.saxutils import prepare_input_source

from flask import Flask


name = "AYUSH"
addreess = "IIT MADRAS, Chennai, TN"

len_add = len(addreess)
print(len_add)

# string index (starts from 0 always)
# A Y U S H
# 0 1 2 3 4

# 2. Numbers (int, flloat)
num = 5
num_float = 5.56
print(type(num), type(num_float))
print(type(pi))

long_float = 5.567890
rounded_long_float = round(long_float, 3)
print(rounded_long_float)

# 3 Booleans
# True or False
is_qualified = False
is_qualified = True


# 4. Lists
my_list = [1, 2, 3, "IITM", True]
print(my_list)
# lists are not fixed in length
my_list += [4]
print(my_list)

print(len(my_list))

#       [1, 2, 3, "IITM", True, 4]
# index: [0, 1, 2, 3       4,   5]
# index: [..  -5 -4  -3     -2    -1]

# sub_list
print(my_list[0:1])
# name_list[start:end] means from start to end - 1
print(my_list[0], my_list[3])

print(my_list[0:5:2])  # 0 -> 4 : 0, 2, 4
print(my_list[0:5:1])  # 0 -> 4 : 0, 1, 2, 3, 4
print(my_list[0:5:3])  # 0 -> 4 : 0, 3
print(my_list[::-1])  # reversing array



strings = 'abcdef'
print(strings[0:4]) # name_String(start, end) : start to end-1 0 to 3rd index