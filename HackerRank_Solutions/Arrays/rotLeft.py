import math

def rotLeft(a, d):
    sets = math.gcd(len(a), d)

    for setPosition in range(sets) :
        temp = a[setPosition]
        positionToShift = setPosition
        completeShift = False
        while completeShift == False :
            nextPosition = positionToShift + d
            if (nextPosition >= len(a)) :
                nextPosition = nextPosition % len(a)

            if (nextPosition != setPosition) :  
                a[positionToShift] = a[nextPosition]
                positionToShift = nextPosition 
            else :
                completeShift = True
        a[positionToShift] = temp
    return a 