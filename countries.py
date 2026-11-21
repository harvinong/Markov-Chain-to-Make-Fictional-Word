from makeAWord import RandomWordGenerator
from string import capwords
import similarity as s

established: set[str] = set()
just_words: set[str] = {"land", "lands", "isle", "isles", "union", "unions", "kingdom", "name", "dom", "rus", "den", "western territory", "car"}
with open("texts/countries.txt") as file:
    for country in file:
        country = country.strip().lower()
        established.add(country)

rwg = RandomWordGenerator("chains/countries-dist.json")
countrySet: set[str] = set()
SIMILARITY = 0.7
def generateCountry(depth: int, similarity: float = SIMILARITY) -> str:
    """generate the country based on the provided Markov's Chain

    Args:
        depth (int): the depth of the token considered. Longer depth gives convincing but restrictive result.
        similarity (float, optional): The threshold of how similar the resulting country can be. Defaults to SIMILARITY.

    Returns:
        str: The randomly generated country.
    """
    country = rwg.makeWord(depth = depth)
    while not all([s.jaccard_similarity(country, x) <= similarity for x in established | just_words]):
        country = rwg.makeWord(depth = depth)
    return capwords(country)

if __name__ == "__main__":
    N = 16
    print(f"\33[33;1mTop {N} countr{'ies' if N != 1 else 'y'} you should visit! :D\33[m")
    while len(countrySet) < N:
        country = generateCountry(4)
        if country.lower() not in countrySet|established|just_words: # and all([s.jaccard_similarity(country, x) <= SIMILARITY for x in established | just_words]):
            print(f"{len(countrySet) + 1:>2}. {country}")
            countrySet.add(country.lower())
