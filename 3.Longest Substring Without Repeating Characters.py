class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary to store the last index of each character in the string
        char_index = {}
        max_length = 0
        start = 0  # Start of the sliding window

        for end in range(len(s)):
            # If the character is already in the dictionary and its index is greater than or equal to the start
            if s[end] in char_index and char_index[s[end]] >= start:
                # Move the start of the window to the next index of the repeating character
                start = char_index[s[end]] + 1

            # Update the last index of the current character
            char_index[s[end]] = end

            # Update the maximum length
            max_length = max(max_length, end - start + 1)

        return max_length
