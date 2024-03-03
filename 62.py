def uniquePaths(m, n):
    # Create a grid to store the number of paths to reach each cell
    dp = [[0] * n for _ in range(m)]

    # There is only one way to reach any cell in the first row or first column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Calculate the number of unique paths for each cell in the grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Return the number of unique paths to reach the bottom-right corner
    return dp[m - 1][n - 1]

# Example usage
m = 3
n = 7
print(uniquePaths(m, n))  # Output: 28
