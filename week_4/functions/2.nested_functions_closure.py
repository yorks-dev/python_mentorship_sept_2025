def make_multiplier(x):

    def multiply(y):  # remembers varuable x inthe scope of make_multiplier
        #  (it as created inside make multiplier)
        return x * y

    return multiply


times3 = make_multiplier(3)
# get a function called multiply which expects a value
print(times3)
print(times3(10))
print(make_multiplier(5)(10))

# make multipler returns a function that expects a value (y) and returns
# 3 * y (the expected value)

# NOTE :  Closure = function that remembers variables from the
# scope in which it was created, even after that scope is gone.
