def repeatedString(s, n):
    finite = 0
    string_count = 0
    remainder_count = 0
    modified_string = ''
    lengthened = 0
    for i in range(len(s)) :
        if (s[i] == 'a') :
            finite += 1
    string_count = n // len(s)
    remainder_count = n % len(s)
    
    lengthened = string_count * finite

    for i in range(remainder_count) :
         if (s[i] == 'a') :
            lengthened += 1       

    return lengthened