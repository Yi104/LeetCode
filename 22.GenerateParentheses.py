from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate("", n, n, result)
        return result
    
    def generate(self, current, left, right, result):
        # Base case: when both left and right parentheses are used up
        if left == 0 and right == 0:
            result.append(current)
            return
        
        # Add left parenthesis if available
        if left > 0:
            self.generate(current + '(', left - 1, right, result)
        
        # Add right parenthesis if available and it doesn't violate the well-formed condition
        if right > 0 and left < right:
            self.generate(current + ')', left, right - 1, result)

# Example usage:
solution = Solution()
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(1))
