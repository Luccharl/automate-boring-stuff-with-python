import pprint

def character_count(text):
    char_count = {}

    for character in text:
        char_count.setdefault(character, 0)
        char_count[character] = char_count[character] + 1
    return char_count

text = '''It was a bright cold day in April, and the 
clocks were striking thirteen.'''

#pprint function makes output much more cleaner
pprint.pprint(character_count(text))

