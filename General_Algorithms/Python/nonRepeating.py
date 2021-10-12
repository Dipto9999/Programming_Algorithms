def non_repeating(s) :
    s = s.replace(' ','').lower()
    char_count = {}

    for c in s :
        if c in char_count :
            char_count[c] += 1
        else :
            char_count[c] = 1

    uniques = ''
    char_sorted = sorted(char_count.items(), key = lambda x : x[1])

    for item in char_sorted :
        if item[1] == 1 :
            uniques += item[0] + ', '
    return_string = ''
    for i in range(0, len(uniques) - 2) :
        return_string += uniques[i] 
 
    return return_string
print(non_repeating('I apple Ape peels'))