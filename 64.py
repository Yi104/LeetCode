def minPathSum(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Initialize a 2D list to store the minimum path sums
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the first cell with the value of the first cell in the grid
    dp[0][0] = grid[0][0]

    # Fill the first row
    for i in range(1, cols):
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    # Fill the first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill the rest of the dp table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[rows - 1][cols - 1]

# Example usage:
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))  # Output should be 7
