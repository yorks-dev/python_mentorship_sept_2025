# Primitive types
# int, float, bool, str

# Dynamic
from numpy import add


x = 10  # x is treated as a dynamic variable why ? because its data type can change
x = str(10)

# list, set, dict, tuple


def add_number(a: int, b: int) -> int:
    return a + b


a, b = 5, 7
if type(a) == type(b) == int:  # static type checking
    print(add_number(a, b))
