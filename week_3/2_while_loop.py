# while (condition):    for the loop to continue we need to condition to be true.
#    TODO

i = 0
while i <= 5:
    # print(i)
    i += 1  # always need to increment this counter on which condition is based on.

#  how do we know if the loop ran as intended (it did not break suddently)
#  how do we know that the loop did not stop in the middle .

list1 = [6, 7, 8, 9, 10]

i = 0
while i <= len(list1) - 1:
    print(list1[i])
    i += 1  # the loop ran perfectly. did not get stoppd in the middle
else:
    print("Loop ran perfectly")
