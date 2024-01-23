class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle is an empty string
        if not needle:
            return 0
        
        # Iterate through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if substring starting at index i matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # If no match is found, return -1
        return -1
