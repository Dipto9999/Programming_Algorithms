def maxSubsetSum(arr):
    possible_sum_a = arr[0]
    possible_sum_b = 0

    for i in range(1, len(arr)) :
        if possible_sum_a > possible_sum_b :
            current_max = possible_sum_a
        else :
            current_max = possible_sum_b
        
        possible_sum_a = possible_sum_b + arr[i]    
        possible_sum_b = current_max
    
    return max(possible_sum_a, possible_sum_b)
        