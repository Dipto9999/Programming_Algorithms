def pair_sum(array, k) :
    if len(array) < 2 :
        return print('Too Small')

    seen = set()
    output = []

    for num in array :
        target = k - num

        if target not in seen :
            seen.add(num)
        else :
            output.append((min(num,target), max(num,target)))

    print('\n'.join(map(str, output)))

pair_sum([1,3,2,2], 4)