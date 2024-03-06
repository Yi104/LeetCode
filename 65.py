import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regular expression pattern to match valid numbers
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return bool(re.match(pattern, s.strip()))

# Example usage:
solution = Solution()
print(solution.isNumber("0"))  # Output: True
print(solution.isNumber(" 0.1 "))  # Output: True
print(solution.isNumber("abc"))  # Output: False
print(solution.isNumber("1 a"))  # Output: False
print(solution.isNumber("2e10"))  # Output: True
