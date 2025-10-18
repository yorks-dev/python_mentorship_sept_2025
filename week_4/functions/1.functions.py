# In python functions are objects
# -> Assign functions to variables
# -> pass them as arguments
# -> return functions from another functions




def greet(name, string,  *numbers ) -> str:  # return types are not strictly checked
    return f"{name}, {string} {numbers}"


print(greet("IITM", "bye.", 0, 6, 7, 9, 10 ))
