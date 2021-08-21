def minimumBribes(q):
    bribes = 0
    message = 'Too chaotic'

    original_positions = q.copy()

    for i in range(len(original_positions)) :
        original_positions[i] = q[i] - 1
 
    for current, original in enumerate(original_positions):

        if original-current > 2:
            bribes = - 1
            break
        for j in range(max(original-1,0), current):
            if original_positions[j] > original:
                bribes += 1
    if (bribes > 0) :
        message = str(bribes)

    print(message)