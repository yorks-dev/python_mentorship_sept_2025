# Name: palindrominator
# Inputs: text:str
# Output: string representing the input string joined with its
# reverse(the last characte should not be repeated twice)



word = "lemon"
# l e m o n
# 0 1 2 3 4
#-5 -4-3-2-1
print(word + word[-2::-1]) 