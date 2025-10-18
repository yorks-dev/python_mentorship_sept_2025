add = lambda a, b: a + b
sub = lambda a, b: a - b
multip = lambda a, b: a * b


def divide(a, b):
    if b != 0:
        return a / b


array_of_functions = [add, sub, multip, divide]
dict_of_functions = {"add": add, "sub": sub, "miltip": multip, "divide": divide}

print(array_of_functions[3](1, 2))
print(dict_of_functions["divide"](5, 5))
print(divide.__name__)  # dunder variable

for function in array_of_functions:
    print(function.__name__)
    if function.__name__ == "divide":
        print(function(10, 2))
