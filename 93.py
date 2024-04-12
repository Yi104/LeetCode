class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return
            for i in range(1, 4):
                if start + i <= len(s):
                    part = s[start:start+i]
                    if 0 <= int(part) <= 255 and (len(part) == 1 or part[0] != '0'):
                        backtrack(start + i, parts + [part])
        
        result = []
        backtrack(0, [])
        return result
