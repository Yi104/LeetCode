def jump(nums):
    if len(nums) <= 1:
        return 0

    jumps = 0
    cur_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest

    return jumps

# Example usage:
nums = [2, 3, 1, 1, 4]
print(jump(nums))  # Output: 2
