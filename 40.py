def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])

    candidates.sort()
    res = []
    backtrack(0, target, [])
    return res

# Example usage:
candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))
