# These let you handle variable-length arguments dynamically.
# in case your function does not know ho many variables it will get


# def demo(*args, **kwargs):
#     # args - tuple of positional arguments
#     # kargs -  dict of keyword arguments
#     print(args)
#     print(kwargs)


# demo(3, 4, 5, name="IITM", rank=1)

import stat


def func(*args, **kwargs):
    # print(age, state)
    if "name" in kwargs:
        print(f"name : {kwargs["name"]}")
    if "rank" in kwargs:
        print(f"rank : {kwargs["rank"]}")
    print(kwargs)

    age, state, *other_args= args
    print(age, state)
    print(other_args)
    
func(20, "WB", 55, 66, name="Ayush", rank=20, age_backup=21)