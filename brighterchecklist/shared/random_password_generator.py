import random

def random_password(length_of_password):
    """Generates a random password of a selected length."""

    return_password = ''

    letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = letters.upper()
    numbers = '1234567890'
    symbols = """!@#$%^&*()`~;'[]:"{}\|/?,.<>"""

    list_of_symbols = [letters, upper_letters, numbers, symbols]

    random.seed()

    for i in range(length_of_password):
        character_list = random.choice(list_of_symbols)
        character = random.choice(character_list)

        return_password += character

    return return_password