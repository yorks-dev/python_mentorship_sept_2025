# Length of longest word in a list
list1 = ["hi", "hello", "awesome", "great", "fantastic"]

longest_length = 0

for word in list1:
    if len(word) > longest_length:
        longest_length = len(word)

print(longest_length)
