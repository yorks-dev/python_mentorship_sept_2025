list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  find the permutations of the list num (2 number)

#  (1, 2) , (1, 3), (1, 4)
counter = 0
for i in list_num:
    for j in list_num:
        if i != j:
            counter += 1
            print(f"({i}, {j})")

print(counter)

# insert variables in a string
# my name is []. I study at []
name = "Ayush"
college = "IITM"
percentage = 0.90
print(f"My name is {name}. I study at {college}. I scored {percentage * 100} %")

list1 = [1, 2, 3, 4, 5]
var = ["Ayush", "James", "Joe"]

for name in var:
    for i in list1:
        print(f"{name} : {i}")

list3 = [4, 5, 6, {"a": 2, "b": [(1, 2, 3), (4, 5, 6)]}]
list3[3]["b"][1] = (6, 7, 8)

print(f"{var[0]} is {list3[3]["b"][1][-1]}")
