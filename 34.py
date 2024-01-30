class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first_occurrence(nums, target):
            start, end = 0, len(nums) - 1
            result = -1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    result = mid
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return result

        def find_last_occurrence(nums, target):
            start, end = 0, len(nums) - 1
            result = -1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    result = mid
                    start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return result

        first_occurrence = find_first_occurrence(nums, target)
        last_occurrence = find_last_occurrence(nums, target)

        return [first_occurrence, last_occurrence]

# Example usage:
solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
print(solution.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
print(solution.searchRange([], 0))  # Output: [-1, -1]
