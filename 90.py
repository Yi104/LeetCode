def subsetsWithDup(nums):
    def backtrack(start, path):
        result.append(path[:])  # Add the current subset to the result
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Include the current element in the subset
            path.append(nums[i])
            # Explore further possibilities with the current subset
            backtrack(i + 1, path)
            # Backtrack: Remove the current element from the subset
            path.pop()

    result = []
    nums.sort()  # Sort the input array
    backtrack(0, [])
    return result

# Example usage:
nums = [1, 2, 2]
print(subsetsWithDup(nums))
