class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Read in and ignore any leading whitespace.
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Step 2: Check for the sign.
        sign = 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Read in digits until a non-digit character is encountered.
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before updating the result.
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return sign * (2**31 - 1) if sign == 1 else sign * (2**31)
            
            result = result * 10 + digit
            i += 1
        
        # Step 4: Adjust sign and return the result.
        return sign * result

# Example usage:
solution = Solution()
print(solution.myAtoi("42"))          # Output: 42
print(solution.myAtoi("   -42"))      # Output: -42
print(solution.myAtoi("4193 with words"))  # Output: 4193
