# items are unique inside a set
set1 = set()
set2 = {1, 2, 3, 4, 5, 5, -1}  # no dublicates
print(set2)

print(len(set2))
set2.add(55)  # elements are not ordered

# set2[0] = 5  # unorderd. type error
returned_value = set2.pop()
print(returned_value, "removed from ", set2)
if -5 in set2:
    set2.remove(-5)  # works, but raises key error
print(set2)
set2.discard(-10)  # safe. does not raise key error
print(set2)


# maths ways of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
set3 = {4}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set3.issubset(set2))
print(set2.issuperset(set3))
print(set3.isdisjoint(set1))  # nothing in common

set1 = {1, 2}
set2 = set1
print(set1 is set2)
