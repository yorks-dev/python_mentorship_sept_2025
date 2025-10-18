file = open("5.txt", "r")

line = file.readline()  # read the first line
print(line)

while line:
    print(file.readline())
