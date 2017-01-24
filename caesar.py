def alphabet_position(character):
    abc = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    loweredcharacter = character.lower()
    # if loweredcharacter not in abc:
    #     return
    for character in abc:
        if character == loweredcharacter:
            return counter
        counter += 1


def rotate_character(character, rotnum):
    abc = "abcdefghijklmnopqrstuvwxyz"
    if character.lower() not in abc:
        return character
    oldcharpos = alphabet_position(character)
    newcharpos = (oldcharpos + rotnum) % len(abc)
    if character.isupper():
        return abc[newcharpos].upper()
    return abc[newcharpos]

def encrypt(text, rotnum):
    newtext = ""
    rotnum = int(rotnum)
    for character in text:
        newcharacter = rotate_character(character, rotnum)
        newtext += newcharacter
    return newtext
