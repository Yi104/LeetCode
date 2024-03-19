def subsets(nums):
    def backtrack(start, path):
        # Add the current subset to the result
        result.append(path[:])
        
        # Explore all possible subsets from the current index onwards
        for i in range(start, len(nums)):
            # Choose
            path.append(nums[i])
            
            # Explore
            backtrack(i + 1, path)
            
            # Unchoose
            path.pop()
    
    result = []
    backtrack(0, [])
    return result

# Example usage:
nums = [1, 2, 3]
print(subsets(nums))
