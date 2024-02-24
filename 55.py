def canJump(nums):
    max_reachable = 0
    n = len(nums)
    
    for i in range(n):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])
        
        if max_reachable >= n - 1:
            return True
    
    return False

# Example usage:
nums = [2,3,1,1,4]
print(canJump(nums))  # Output: True
