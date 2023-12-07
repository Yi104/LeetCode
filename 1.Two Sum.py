def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_indices:
            # Found a pair that adds up to the target
            return [num_indices[complement], i]

        # If not, add the current number and its index to the dictionary
        num_indices[num] = i

    # No solution found
    raise ValueError("No solution found for the given input.")

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
