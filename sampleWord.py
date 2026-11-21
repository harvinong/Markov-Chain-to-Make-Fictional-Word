import random

with open("popular.txt") as source, open("sample.txt", "w") as dest:
    words: list[str] = []
    for word in source:
        word = word.strip()
        if len(word) == 0: continue
        words.append(word)

    for word in random.choices(words, k = 16):
        dest.write(word)
        dest.write("\n")
    
