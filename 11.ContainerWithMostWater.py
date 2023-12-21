from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            # Move the pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Example usage:
solution = Solution()
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height2 = [1, 1]

print(solution.maxArea(height1))  # Output: 49
print(solution.maxArea(height2))  # Output: 1
