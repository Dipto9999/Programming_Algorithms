def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)

    minimum_difference = math.inf   
    for i in range(len(arr) - 1) :
        minimum_difference = min(minimum_difference, abs(sorted_arr[i] - sorted_arr[i + 1]))
    return minimum_difference
