from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Check if the array is empty
        if not nums:
            return 0

        # Initialize the pointer to track unique elements
        unique_ptr = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Compare the current element with the previous one
            if nums[i] != nums[unique_ptr]:
                # Update the next unique element
                unique_ptr += 1
                nums[unique_ptr] = nums[i]

        # Return the count of unique elements
        return unique_ptr + 1
