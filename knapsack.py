# Start
# Read n items, their values and weights, and knapsack capacity W
# Make a table dp[n+1][W+1] and fill it with 0
# For each item i from 1 to n:
# For each weight w from 1 to W:
# If weights[i-1] ≤ w:
# dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
# Else:
# dp[i][w] = dp[i-1][w]
# Print dp[n][W] as maximum value
# Stop

def knapsack(values, weights, W):
    n = len(values)
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print("Maximum value:", knapsack(values, weights, W))
