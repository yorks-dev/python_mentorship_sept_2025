# given a file, and from that file we have to read each line and then calculate the total cost


file = open("5.csv", "r")

lines = file.read()  # read the whole file at once
list_array = (lines.split("\n"))[1:]  # array of all lines except 1st lines
total_price = 0
print(list_array)

for line in list_array:
    line_arr = line.split(",")
    print(line_arr)
    name = line_arr[0]
    price = line_arr[1]
    quantity = line_arr[2]

    total_price += float(price) * float(quantity)

print(total_price)
