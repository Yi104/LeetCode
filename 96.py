def numTrees(n):
    if n == 0 or n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    
    return dp[n]

# Test the function
n = 3
print("Number of unique BSTs with", n, "nodes:", numTrees(n))
