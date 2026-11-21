from random import choice
from names import generateName
from countries import generateCountry

def greet(name: str, country: str) -> str:
    """Make a random greetings with names and country of origin.

    Args:
        name (str): Full name of the person
        country (str): Country the person is originated from

    Returns:
        str: Full greetings, with salutation, name, country, along with appropriate punctuations and transitions.
    """
    intros = ["Hello", "Good morning", "Good afternoon", "Good afternoon", "Salutations", "Greetings", "Hi", "Hiya", "Heyo"]
    intro_body = ["! ", ", ", ". ", "... ", "? "]
    bodies = ["my name is {}", "i am {}", "call me {}", "{} is my name", "{} here"]
    body_outro = ["! ", ", and ", ". ", "... ", "... and "]
    outros = ["I am from {}", "I live in {}", "I originated in {}", "I was born in {}", "{} is my lovely country"]
    punctuations = ["! ", ". ", "... "]

    intro = choice(intros)
    in_body = choice(intro_body)
    body = choice(bodies)
    if in_body.strip() in "?!...": body = body.capitalize()
    body = body.format(name)
    body_out = choice(body_outro)
    outro = choice(outros)
    if body_out.strip() in "?!.": outro = outro.capitalize()
    outro = outro.format(country)
    punc = choice(punctuations)

    return intro + in_body + body + body_out + outro + punc

if __name__ == "__main__":
    for i in range(16):
        name = generateName(4)
        country = generateCountry(5)

        print(f"{i + 1:>2}. " + greet(name, country))