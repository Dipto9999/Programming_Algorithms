def minimumSwaps(arr):
    swaps = 0

    for i in range(len(arr)) :
        while arr[i] != (i + 1) :
            correct_position = arr[i] - 1
            arr[correct_position], arr[i] = arr[i], arr[correct_position]
            swaps += 1
    return swaps