def getMinimumCost(k, c):
    modified_c = sorted(c)

    friend_purchases = [0] * k
    cost = 0
    friend = 0
    for i in range(len(modified_c)) :
        effective_i = len(modified_c) - i - 1
        cost += (friend_purchases[friend] + 1) * modified_c[effective_i]
        
        friend_purchases[friend] += 1
        friend += 1
        if friend == k :
            friend = 0
    return cost