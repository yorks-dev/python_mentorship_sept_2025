list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in list1:
    for j in i:
        # print(j)
        pass

for i in range(10):  # 0 to 9
    for j in range(i):  #  0 to what ever i-1 is
        print(f"{i}:{j}")

# i : 0
# j : 0 to 0 - 1 : nothing

# i : 1
# j : 0 to 1-1 : 0 to 0  : 0

# i = 2
# j : 0 to 2-1 : 0 to 1

# ...

# i = 5
# j : 0 to 5-1 : 0 to 4
# ...
