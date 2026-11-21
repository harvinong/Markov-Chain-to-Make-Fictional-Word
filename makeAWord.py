import random
import json

DEPTH: int = 3

class RandomWordGenerator:
    dist: dict[str, dict[str, int]]

    def __init__(self, filename: str = "dist.json") -> None:
        with open(filename) as src:
            self.dist = json.load(src)


    def _pickRandomLetter(self, token: str) -> str:
        if len(token) == 0: return random.choice([chr(ord('a') + i) for i in range(26)] + [""])
        total = 0
        freqTable: dict[str, int]|None = self.dist.get(token)

        if freqTable is None:
            return self._pickRandomLetter(token[1:])
        
        for freq in freqTable.values():
            total += freq

        roll = random.randint(1, total)

        for letter, freq in freqTable.items():
            roll -= freq
            if roll <= 0:
                return letter

        return ""
        
    def makeWord(self, startingLetter: str = "", depth: int = DEPTH):
        # Normalize argument
        if len(startingLetter) == 0:
            startingLetter = chr(random.randint(ord('a'), ord('z')))

        startingLetter = startingLetter.strip().lower()
        
        # if startingLetter[-depth:] not in dist:
        #     if depth == 0:
        #         return ""
        #     return startingLetter[:1-depth] + makeWord(startingLetter[1-depth:])
        
        # build the word
        word: str = startingLetter
        nextLetter = None


        while nextLetter is None or len(nextLetter) > 0:
            token: str = word[-depth:]
            nextLetter = self._pickRandomLetter(token)
            word += nextLetter

        if len(word) > 1:
            return word
        else:
            return self.makeWord()
    
if __name__ == "__main__":
    rwg = RandomWordGenerator()
    i = 0
    while i < 16:
        word = rwg.makeWord()
        # if len(word) < 2: continue
        print(word)
        i += 1
    # for suffix in ["dia", "land", "stan"]:
    #     i = 0
        # while i < 3:
        #     country = makeWord()
        #     if country[-len(suffix):] != suffix: continue
        #     if len(country[:-len(suffix)]) < 2: continue
        #     print(country)
        #     i += 1