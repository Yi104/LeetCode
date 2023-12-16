class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special case: Negative numbers are not palindromes
        if x < 0:
            return False

        # Reverse the digits of the number
        reversed_number = 0
        original_x = x
        while x != 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10

        # Check if the reversed number is equal to the original number
        return original_x == reversed_number
