#!/bin/python3

import math

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    types = []
    for i in range(len(ar)) :
        pair = 0
        contains = 0
        for k in range(i) :
            if ar[k] == ar[i] :
                contains = 1
        
        if (contains == 0) :
            for j in range(i, len(ar)) :
                if (ar[i] == ar[j]) :
                    pair += 1 
        count += int(pair/2)  
    return count

sockMerchant(5, [2,2,3,3,4])
