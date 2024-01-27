from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1

        # Find the first pair of consecutive elements nums[i-1] and nums[i] such that nums[i-1] < nums[i]
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            # If no such pair is found, reverse the entire array
            nums.reverse()
            return

        j = n - 1
        # Find the first element nums[j] that is greater than nums[i-1]
        while nums[j] <= nums[i-1]:
            j -= 1

        # Swap nums[i-1] and nums[j]
        nums[i-1], nums[j] = nums[j], nums[i-1]

        # Reverse the subarray to the right of nums[i-1]
        nums[i:] = reversed(nums[i:])
