from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                current_count[word] += 1

                while current_count[word] > word_count[word]:
                    current_count[s[left:left + word_len]] -= 1
                    left += word_len

                if right - left == total_len:
                    result.append(left)

        return result
