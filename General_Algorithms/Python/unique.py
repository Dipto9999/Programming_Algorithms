def unique(string) :
    string.replace(' ','').lower()
    characters = set()

    for letter in string :
        if letter in characters :
            return False
        else :
            characters.add(letter)

    return True

print(unique('a bb cdef'))