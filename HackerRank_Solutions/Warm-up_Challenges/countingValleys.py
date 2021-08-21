def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    inValley = False
    current_displacement = 0
    for i in range(len(path)) :
        if path[i] == 'U' :
            current_displacement += 1
        elif path[i] == 'D' :
            current_displacement -= 1             
        if current_displacement < 0 :
            if inValley == False :
                valleys += 1
            inValley = True
        else :
            inValley = False
    return valleys
