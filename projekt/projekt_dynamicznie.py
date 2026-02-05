def knapSack(W, wt, val, n): 
    
    dp = [0 for i in range(W+1)] 

    for i in range(1, n+1): 
        for w in range(W, 0, -1): 
            if wt[i-1] <= w: 
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1]) 
    return dp[W] 


if __name__ == '__main__': 
    profit = [3, 4, 5, 8]
    weight = [2, 3, 4, 5]
    W = 8

    n = len(profit) 
    print(knapSack(W, weight, profit, n))


