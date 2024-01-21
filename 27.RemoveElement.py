from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a variable to keep track of the count of elements not equal to val
        k = 0
        
        # Iterate through the elements of nums
        for num in nums:
            # If the current element is not equal to val, update nums[k] and increment k
            if num != val:
                nums[k] = num
                k += 1
        
        # Return the count of elements not equal to val
        return k
