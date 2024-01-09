from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to letters
        digit_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, current):
            if index == len(digits):
                result.append(''.join(current))
                return

            for letter in digit_letters[digits[index]]:
                current.append(letter)
                backtrack(index + 1, current)
                current.pop()

        result = []
        backtrack(0, [])
        return result

# Example usage:
solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
print(solution.letterCombinations("2"))
