def isScramble(s1: str, s2: str) -> bool:
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False
    
    n = len(s1)
    # dp[i][j][k] represents whether s2[j:j+k+1] is a scrambled string of s1[i:i+k+1]
    dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

    for k in range(1, n + 1):
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                if k == 1:
                    dp[i][j][k] = s1[i] == s2[j]
                else:
                    for m in range(1, k):
                        if (dp[i][j][m] and dp[i + m][j + m][k - m]) or \
                                (dp[i][j + k - m][m] and dp[i + m][j][k - m]):
                            dp[i][j][k] = True
                            break
    return dp[0][0][n]

# Example usage:
s1 = "great"
s2 = "rgeat"
print(isScramble(s1, s2))  # Output: True
