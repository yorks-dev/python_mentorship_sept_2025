# List
arr = ["Ayus", "IITm"]

arr.append("8")  # type checking. Makes sure the data types is same
arr += ["IITD"]

print(arr)
arr.pop(0)
print(arr)

arr = [5, 6, 7, 8, 9]
# arr.remove(-2)  # raise a value error (removes using value)
print(arr)
arr.pop(-2)  # removes using index
print(arr)

# safe value error
arr = [1, 2, 3, 4, 6]
print(5 in arr)  # remove it only if that element exists

item_to_remove = 5
if item_to_remove in arr:
    arr.remove(5)

print(arr)
print(len(arr))
arr[0] = -5

arr1 = [1, 2, 3]  # modified in place
arr2 = [4, 5, 6]
print(arr1.extend(arr2))  # does not return a new array, just extending
print(arr1)


# looping through list
for item in arr1:
    print(item)
