def luckBalance(k, contests):
    important_scores = []
    luck = 0
    for i in range(len(contests)) :
        if contests[i][1] == 1 :
            important_scores.append(contests[i][0])
        else : 
            luck += contests[i][0]
    
    important_scores = sorted(important_scores, reverse=True)
    for i in range(len(important_scores)) :
        if i < k :
            luck += important_scores[i]
        else :
            luck -= important_scores[i]
    return luck