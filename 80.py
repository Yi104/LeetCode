def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    
    # Slow pointer
    slow = 2
    
    # Fast pointer
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
            
    return slow
