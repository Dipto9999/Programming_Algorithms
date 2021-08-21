def twoStrings(s1, s2):
    ALPHABET = 26
    letters_s1 = ALPHABET*[0]
     
    for i in range(len(s1)) :
        letter = ord(s1[i]) - ord('a')
        letters_s1[letter] += 1
        
    for i in range(len(s2)) :
        letter = ord(s2[i]) - ord('a')
        if letters_s1[letter] != 0 :
            return 'YES'
    return 'NO'