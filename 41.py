def firstMissingPositive(nums):
    n = len(nums)
    
    # Step 1: Replace negative numbers and zeros with n+1
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
            
    # Step 2: Mark present numbers
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first missing positive
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    # Step 4: If all numbers are present, return n + 1
    return n + 1

# Example usage
nums = [3, 4, -1, 1]
print(firstMissingPositive(nums))  # Output: 2
