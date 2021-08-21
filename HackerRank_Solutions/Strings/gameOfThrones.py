def gameOfThrones(s):
    # Write your code here

    letters_available = {}

    for letter in s :
        if (letter in letters_available) :
            letters_available[letter] += 1
        else :
            letters_available[letter] = 1

    odd_count = 0
    for letter, frequency in letters_available.items() :
        if frequency % 2 == 1 :
            odd_count += 1
        if odd_count > 1 :
            return 'NO'
    return 'YES'

print(gameOfThrones('aaabbbb'))