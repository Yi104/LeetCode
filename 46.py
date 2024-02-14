class Solution:
    def permute(self, nums):
        def backtrack(nums, path, result):
            if not nums:
                result.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]], result)

        result = []
        backtrack(nums, [], result)
        return result

# Example usage:
nums = [1, 2, 3]
solution = Solution()
print(solution.permute(nums))
