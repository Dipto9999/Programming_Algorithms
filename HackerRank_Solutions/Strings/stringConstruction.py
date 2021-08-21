def stringConstruction(s):
    cost = 0
    letters = {}

    for letter in s :
        if letter in letters :
            letters[letter] += 1
        else :
            letters[letter] = 1
            cost += 1
    return cost