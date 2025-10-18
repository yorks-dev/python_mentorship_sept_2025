# not changable, immutable, once you define it cant change evr . ever, ordered
# like lists but once its defined cant change it again

from itertools import count


t = (1, 2, 3, 4, 5, 5, "hi", [1, 2], (2, 3))
# t[0] = 88  # immutable
t1 = ()  # empty tupple
t2 = (8,)  # single valued tuple
print(t[0])

t = (1, 2, -1, -2, 8, 1, 8)
print(sorted(t))
t_return = tuple(sorted(tuple(list(t))))  # sorted returns a list
print(t_return)

# i want to remove dublicates
set_t = set(t)
print(tuple(set_t))

a = (1, 2)
b = (3, 5)
print(a * 2)  # repeat the tuple multiple time

# Tupele unpacking
person = ("John", 25, "North Korea")
name, age, country = person
print(name, age, country)

person = ("John", 25, ("Pyongyang", "North Korea"))
name, age, (city, country) = person
print(name, age, (city, country))
print(city, country)
