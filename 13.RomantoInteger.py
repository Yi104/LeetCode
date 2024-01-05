class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        # Iterate through the string from left to right
        for i in range(len(s)):
            # Check if the current numeral is smaller than the next numeral
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]

        return result

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))     # Output: 3
print(solution.romanToInt("LVIII"))   # Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994
