from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    target_counts = Counter(t)
    required_chars = len(target_counts)
    formed_chars = 0
    window_counts = {}
    left = 0
    min_len = float('inf')
    min_window = ""

    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed_chars += 1

        while formed_chars == required_chars and left <= right:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]

            window_counts[s[left]] -= 1
            if s[left] in target_counts and window_counts[s[left]] < target_counts[s[left]]:
                formed_chars -= 1
            left += 1

    return min_window

# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # Output should be "BANC"
