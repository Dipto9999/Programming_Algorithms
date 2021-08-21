def maxMin(k, arr):
    sorted_arr = sorted(arr)

    offset = 0
    unfairness = math.inf

    for i in range(len(arr) - k + 1) :
        unfairness = min(unfairness, (sorted_arr[i + k - 1] - sorted_arr[i]))
    return unfairness