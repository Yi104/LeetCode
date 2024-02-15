class Solution:
    def permuteUnique(self, nums):
        def backtrack(path, counter):
            if len(path) == len(nums):
                permutations.append(path[:])
                return
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[num] += 1

        permutations = []
        backtrack([], collections.Counter(nums))
        return permutations
