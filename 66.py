def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10
        if carry == 0:
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits

# Example usage:
digits = [1, 2, 3]
print(plusOne(digits))  # Output: [1, 2, 4]
