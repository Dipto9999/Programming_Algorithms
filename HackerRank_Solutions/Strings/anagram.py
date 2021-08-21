def makingAnagrams(s1, s2):
    letters_s1 = {}
    letters_s2 = {}
    reductions = 0

    for letter in s1 :
        if letter in letters_s1 :
            letters_s1[letter] += 1
        else :
            letters_s1[letter] = 1

    for letter in s2 :
        if letter in letters_s2 :
            letters_s2[letter] += 1
        else :
            letters_s2[letter] = 1

    for letter, count in letters_s1.items() :
        if not (letter in letters_s2) :
            reductions += count
        elif (letters_s2[letter] != count) :
            difference = abs(count - letters_s2[letter])
            reductions += difference

    for letter, count in letters_s2.items() :
        if not (letter in letters_s1) :
            reductions += count

    return reductions