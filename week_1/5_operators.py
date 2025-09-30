# Operators

# 1. Arithmetic operators
from traceback import print_tb
from numpy import not_equal


num = (5 * 5) + 7 - 2 / 4
#  BDMAS rule
# 25 + 7 - 0.5 = 31.5

value = 7 / 2  # 5.0 float values
print(value)
value2 = 7 // 2  # floor_division
print(value2)
value_rem = 7 % 2
print(value_rem)  # remainder.

print(5**3)


# 2 Comparison Operators (returns true or false)
is_greater = 5 >= 2  # True
is_smaller = 5 < 5  # False
print(is_greater, is_smaller)

is_equal = 5 == 5 # True
not_equal = 5 != 6 # True
print(is_equal, not_equal)
print(not True)

# Logical Operator
# and, or , not

# and -> (if True) and (if True)
# if first is true then check 2nd. if 2nd is true (true and True == True), if false then False.
# if first is false , whole statement is false.
print(True and True)

# or operator
# True or Flase = True
# True or True = True
# True or True = True
# False or False = False

# not
print(not False) # true

# Real life example

age = 15
marks = 25
# for qualified : atleast 17 and 85 marks 
is_qualified_for_college =  (age >= 17) and (marks >= 85)
print(is_qualified_for_college)

grade_12_marks = 56
grade_10_marks = 89
# qualified if either marks >= 85
is_qualified_for_college = (grade_10_marks >= 85) or (grade_12_marks >= 85)
print(is_qualified_for_college)