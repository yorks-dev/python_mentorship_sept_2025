# Caesar Cipher?

string = "abcdefgh"
step = 5
first_letter = ord(string[0]) + 5
print(chr(first_letter))

arr_string = [chr(ord(c) + step) for c in string]
string_cypher = "".join(arr_string)
print(string)
print(string_cypher)

# friend will do this
cypher_array = [chr(ord(c) - step) for c in string_cypher]
print(cypher_array)
original_string = "".join(cypher_array)
print(original_string)
