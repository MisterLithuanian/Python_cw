def knapSack(wt, val, W, n): 
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 
    if wt[n-1] <= W: 
        t[n][W] = max( 
            val[n-1] + knapSack( 
                wt, val, W-wt[n-1], n-1), 
            knapSack(wt, val, W, n-1)) 
        return t[n][W] 
    elif wt[n-1] > W: 
        t[n][W] = knapSack(wt, val, W, n-1) 
        return t[n][W] 

profit = [100, 200, 300] 
weight = [10, 20, 30] 
W = 100
n = len(profit) 
t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
print(knapSack(weight, profit, W, n)) 
