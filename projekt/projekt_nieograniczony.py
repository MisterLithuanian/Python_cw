def unbounded_knapSack(weights, profit, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(capacity + 1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + profit[j])

    return dp[capacity]

if __name__ == '__main__': 
    profit = [100, 200, 300] 
    weight = [10, 20, 30] 
    W = 100
    print(unbounded_knapSack(weight, profit, W)) 