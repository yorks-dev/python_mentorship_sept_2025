# given a string count the number of characters until you hit a user given character.


from re import L


string = "this is IIT madras, 1 the best university in india"
#  user gives input as m
# count the number of characters befor that m

user_input = input("Enter character : ")
if not len(user_input) == 1:
    print("wrong input")
else:
    string = string.lower()
    user_input = user_input.lower()

    if user_input in string:

        index_of_user_input = string.index(
            user_input
        )  # this raises a error if it cant find anything

        print(string[0:index_of_user_input])
        print(len(string[0:index_of_user_input]))
    else:
        print("User input does not exist in the stirng")
