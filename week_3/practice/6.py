# output has to be
# Alice scored 85
# Bob scored 78
# Charlie scored 92

from numpy import flip


file = open("6.csv", "r")

# skip header
file.readline()

line = file.readline()  # reads second line
while line:
    data = line.strip().split(",")
    name = data[0]
    marks = data[2]
    print(name, "scored", marks)
    line = file.readline()  # dont forget to go to the next line

file.close()
