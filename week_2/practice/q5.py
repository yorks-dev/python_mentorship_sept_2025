# given string i want to check if it has a vowel in it or not.

word = "string"
vowels = ["a", "e", "i", "o", "u"]

for idx, ch in enumerate(word.lower()):
    if ch in vowels:
        print(f"Vowel exists at {idx+1}:{ch}")
        break

# ch : (0, s) , (1, t), (2,r) , (3,i), (4,n) ...


for ch in "string":
    if ch == "r":
        continue    # skip all the statements after the continue statement in the loop
    print(ch)