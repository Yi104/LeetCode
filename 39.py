def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            path.append(candidates[i])
            # Note: The start index remains the same as we can reuse the same element
            backtrack(i, target - candidates[i], path)
            path.pop()

    result = []
    candidates.sort()  # Sort the candidates to handle duplicates and optimize
    backtrack(0, target, [])
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
