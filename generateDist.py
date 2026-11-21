import json

dist: dict[str, dict[str, int]] = {} # distribution table {token: {letter: frequency}}
WORD_BANK = "texts/countries.txt" # List of words, with "\n" separating each word/phrase.
OUT = "chains/countries-dist.json" # Output in .json
MIN_DEPTH = 3
MAX_DEPTH = 5
INCLUDE_NOISE = True # Introduce small amount of noise (latin alphabet)
COUNTER_WEIGHT = 1960 # if noise is includes, add this weight for every occurence of a letter

def getDistOfWord(word: str, depth: int = 1) -> dict[str, dict[str, int]]:
    charDist: dict[str, dict[str, int]] = {}
    # process each char in word
    for i in range(1, len(word)):
        token: str = word[max(0, i-depth):i]
        letter: str = word[i]
        charDist.setdefault(token, {})
        if INCLUDE_NOISE:
            for j in range(26):
                charDist[token].setdefault(chr(ord('a') + j), 1)
        charDist[token].setdefault(letter, 0)
        charDist[token][letter] += COUNTER_WEIGHT if INCLUDE_NOISE else 1

    # add EOL ("") to the last bit of the word
    token: str = word[-depth:]
    letter: str = ""
    charDist.setdefault(token, {})
    if INCLUDE_NOISE:
        for j in range(26):
            charDist[token].setdefault(chr(ord('a') + j), 1)
    charDist[token][letter] = COUNTER_WEIGHT if INCLUDE_NOISE else 1

    return charDist

with open(WORD_BANK) as source, open(OUT, "w") as dest:
    for word in source:
        word = word.strip().lower()
        if len(word) == 0: continue

        for depth in range(MIN_DEPTH, MAX_DEPTH + 1):
            for k, v in getDistOfWord(word, depth).items():
                dist.setdefault(k, {})
                for k0, v0 in v.items():
                    dist[k].setdefault(k0, 0)
                    dist[k][k0] += v0

    json.dump(dist, dest, indent = 4)
    