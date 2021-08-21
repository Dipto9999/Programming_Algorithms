def hourglassSum(arr):
    sums = []
    for row in range(1, 5) :
        for column in range(1, 5) :
            hourglass = 0
            hourglass += arr[row-1][column-1]
            hourglass += arr[row-1][column]
            hourglass += arr[row-1][column+1]
            hourglass += arr[row][column]
            hourglass += arr[row+1][column-1]
            hourglass += arr[row+1][column]
            hourglass += arr[row+1][column+1]
            sums.append(hourglass)
    maximum = sums[0]
    for i in range(len(sums)) :
        if (sums[i] > maximum) :
            maximum = sums[i]
    return maximum
