def makeAnagram(a, b):
    ALPHABET = 26

    letters_a = [0]*ALPHABET
    letters_b = [0]*ALPHABET
    
    decrease = 0

    for i in range(len(a)) :
        character = ord(a[i]) - ord('a')
        letters_a[character] += 1  

    for i in range(len(b)) :
        character = ord(b[i]) - ord('a')
        letters_b[character] += 1  

    for i in range(ALPHABET) :
        if letters_a[i] != letters_b[i] :
            decrease += abs(letters_a[i] - letters_b[i])
    return decrease