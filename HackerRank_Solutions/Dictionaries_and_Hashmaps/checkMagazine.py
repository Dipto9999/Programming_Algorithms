from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    contains = "Yes"
    words_and_count = Counter(magazine)

    for i in range(len(note)) :w
        if words_and_count[(note[i])] > 0 :
            words_and_count[(note[i])] -= 1
        else :
            contains = "No"
    print(contains)