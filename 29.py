class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case where divisor is 0
        if divisor == 0:
            raise ValueError("Cannot divide by zero")

        # Handle overflow cases
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Take the absolute values of dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize the quotient
        quotient = 0

        # Bitwise division
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        return sign * quotient
