def makeAnagram(s):
    if (len(s) % 2 != 0) :
        return -1

    first_string = s[:len(s)//2]
    second_string = s[len(s)//2:]

    different_letters = {}

    change_count = 0

    for letter in first_string :
        if letter in different_letters :
            different_letters[letter] += 1
        else :
            different_letters[letter] = 1

    for letter in second_string :
        if letter in different_letters :
            if (different_letters[letter] != 0) :
                different_letters[letter] -= 1

    for letter, count in different_letters.items() :
        change_count += count

    return change_count

print(makeAnagram('fdhlvosfpafhalll'))