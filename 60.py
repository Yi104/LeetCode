class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * (n+1)
        for i in range(1, n+1):
            factorial[i] = factorial[i-1] * i
        
        nums = [i for i in range(1, n+1)]
        result = []
        
        k -= 1  # 0-based index
        
        for i in range(n, 0, -1):
            index = k // factorial[i-1]
            k %= factorial[i-1]
            result.append(str(nums[index]))
            nums.pop(index)
        
        return ''.join(result)
