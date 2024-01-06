from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Iterate through characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Check if the character is common to all strings
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    # If not, return the common prefix found so far
                    return strs[0][:i]

        # If all characters match, return the entire first string
        return strs[0]

# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))      # Output: ""
