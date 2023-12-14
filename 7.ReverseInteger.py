class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer limits
        int_min, int_max = -2**31, 2**31 - 1

        # Convert the integer to a string for easy reversal
        str_x = str(x)

        # Handle the sign separately
        if x < 0:
            reversed_str = '-' + str_x[:0:-1]  # Reverse and exclude the '-' sign
        else:
            reversed_str = str_x[::-1]  # Reverse the string

        # Convert the reversed string back to an integer
        reversed_x = int(reversed_str)

        # Check if the reversed integer is within the 32-bit signed integer range
        if int_min <= reversed_x <= int_max:
            return reversed_x
        else:
            return 0  # Return 0 if outside the range

# Test the examples
solution = Solution()
print(solution.reverse(123))    # Output: 321
print(solution.reverse(-123))   # Output: -321
print(solution.reverse(120))    # Output: 21
