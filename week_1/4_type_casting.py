#### Type conversions
value = 5  # int
value_str = str(value)  # string
print(type(value), type(value_str))  # always print as string

# input_num = input("Enter number : ")
# input_str = int(input_num)
# print(type(input_num))

# conversion to string.
num = 5
num_str = "num : " + str(num)
print(num_str)

# convert to float
num = 5
num_float = float(5)
print(num_float)  # up casting

num_float = 5.697863
num = int(num_float)  # down casting, loosing decimal places.
print(num)

# conversion to boolean

num = 2  # other then 0, everything else is true
string_1 = "IITM"  # If its not empty then its true.
num2 = 0  # false
string_2 = ""  # false empty string.

print(bool(num), bool(string_1), bool(num2), bool(string_2))
