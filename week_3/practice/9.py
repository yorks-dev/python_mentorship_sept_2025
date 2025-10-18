# given a sentence, we have to reverse the words which have an even length
# i am a really good person
# i ma a yllaer doog nosrep

sentence = input("Give sentence : ")
sentence = sentence.strip()

word_array = sentence.split(" ")

for index in range(len(word_array)):
    if len(word_array[index]) % 2 == 0:  # even
        word_array[index] = word_array[index][::-1]

sentence_reversed = " ".join(word_array)
print(sentence_reversed)
