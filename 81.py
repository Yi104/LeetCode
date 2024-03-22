def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        while left < right and nums[left] == nums[left + 1]:  # Skip duplicates from the left
            left += 1
        while left < right and nums[right] == nums[right - 1]:  # Skip duplicates from the right
            right -= 1
            
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:  # Target lies in the left half
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:  # Target lies in the right half
                left = mid + 1
            else:
                right = mid - 1
    
    return False
