
from math import floor


def getChange(M, P):
                    #0 1  2    3   4   5
    denominations = [1, 5, 10, 25, 50, 100]
    coins = [0 for i in range(len(denominations))]

    
    change = (M*100 - P*100) // 1
    
    while change > 0:
        if change >= 100:
            coins[5] = coins[5] + 1
            change = change - 100
            continue
            
        if change >= 50:
            coins[4] = coins[4] + 1
            change = change - 50
            continue
            
        if change >= 25:
            coins[3] = coins[3] + 1
            change = change - 25
            continue
            
        if change >= 10:
            coins[2] = coins[2] + 1
            change = change - 10
            continue
            
        if change >= 5:
            coins[1] = coins[1] + 1
            change = change - 5
            continue
            
        if change >= 1:
            coins[0] = coins[0] + 1
            change = change - 1
            continue
            
            
    return coins

print(getChange(2, 1.99))
    