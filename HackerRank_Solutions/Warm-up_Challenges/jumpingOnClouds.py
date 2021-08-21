def jumpingOnClouds(c):
    position = 0
    jumps = 0
    while (position < len(c)) :
        if (position + 2 < len(c) and c[position + 2] == 0):
            position += 2
        else :
            position += 1
        if (position != (len(c) - 1)) :
            jumps += 1
    return jumps
