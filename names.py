from makeAWord import RandomWordGenerator
from string import capwords

firstGen = RandomWordGenerator("chains/first-names-dist.json")
lastGen = RandomWordGenerator("chains/last-names-dist.json")

def generateName(depth: int) -> str:
    """Generate a full name, consisting of a first name and a last name.

    Args:
        depth (int): The depth of the token. Higher depth gives more convincing but restrictive result.

    Returns:
        str: full name, with proper capitalization.
    """
    firstName = firstGen.makeWord(depth = depth)
    lastName = lastGen.makeWord(depth = depth)

    return firstName.capitalize() + " " + lastName.capitalize()

if __name__ == "__main__":
    N = 16
    DEPTH = 4
    nameSet: set[str] = set()
    print(f"\33[33;1mTop {N} name{'s' if N != 1 else ''}! :D\33[m")
    while len(nameSet) < N:
        name = generateName(DEPTH)
        if name.lower() not in nameSet:
            print(f"{len(nameSet) + 1:>2}. {name}")
            nameSet.add(name)
