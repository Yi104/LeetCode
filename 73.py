def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)

    # Create a 2D array to store the distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],        # deletion
                                   dp[i][j - 1],        # insertion
                                   dp[i - 1][j - 1])   # substitution

    return dp[m][n]

# Example usage:
word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))  # Output: 3
