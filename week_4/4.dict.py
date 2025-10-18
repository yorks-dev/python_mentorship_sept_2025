# dict is key, value pair

dict_age = {"Ayush": 20, "John": 30, "Rick": 15}
print(dict_age["Ayush"])
print(dict_age["John"])

print(dict_age.keys())
print(dict_age.values())
print(dict_age.items())

for item in dict_age:  # by default iterates over
    print(item)


for name, age in dict_age.items():  # by default iterates over
    print(name, age)


# dict inside dict

dict1 = {"a": 1, "b": 2, "c": {"name": "IITM"}}
dict2 = {("Ayush", 21, "IITM"): 99, ("John", 25, "IITD"): 82}
#  use immutable keys
