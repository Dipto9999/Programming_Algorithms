def anagram(s1, s2) :

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    # Check if same number of letter.s
    if len(s1) != len(s2) :
        return False
    
    # Count frequency of each letter.
    count = {}

    for letter in s1 :
        # For every letter in first string
        if letter in count :
            count[letter] += 1
        else :
            count[letter] = 1
        
    for letter in s2 :
        # Do reverse for second string       
        if letter in count :
            count[letter] -= 1
        else :
            count[letter] = 1
        
    for k in count :
        if count[k] != 0 :
            return False
    return True
    
x = anagram('Clint Eastwood', 'old WEST action')
print(x)