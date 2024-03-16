def sortColors(nums):
    """
    Sorts an array of 0s, 1s, and 2s in-place (Dutch National Flag problem)
    
    Args:
    nums: List[int] -- The array containing 0s, 1s, and 2s
    
    Returns:
    None (modifies the input list in-place)
    """
    left, mid, right = 0, 0, len(nums) - 1
    
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
