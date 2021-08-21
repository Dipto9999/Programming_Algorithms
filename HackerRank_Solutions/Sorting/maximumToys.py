def maximumToys(prices, k):
    sorted_prices = sorted(prices)

    toys = 0
    remaining = k
    for i in range(len(sorted_prices)) :
        if remaining >= sorted_prices[i] :
            remaining = remaining - sorted_prices[i]
            toys += 1
    return toys