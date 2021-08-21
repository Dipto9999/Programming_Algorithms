def isValid(s):
    characters = {}
    count_frequencies = {}


    for i in range(len(s)) :
        if s[i] in characters :
            characters[s[i]] += 1
        else :
            characters[s[i]] = 1


    min_count = characters[s[i]]
    max_count = characters[s[i]]

    for letter, count in characters.items() :
        if count in count_frequencies :
            count_frequencies[count] += 1
        else :
            count_frequencies[count] = 1
        
        if count < min_count :
            min_count = count
        elif count > max_count :
            max_count = count

    if len(count_frequencies) == 1 :
        return 'YES'
    elif len(count_frequencies) == 2 :
        if count_frequencies[max_count] == 1 and max_count - min_count == 1 :
            return 'YES'
        elif count_frequencies[min_count] == 1 and min_count == 1 :
            return 'YES'
    return 'NO'