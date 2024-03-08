def addBinary(a: str, b: str) -> str:
    result = ""
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        total_sum = carry
        
        if i >= 0:
            total_sum += int(a[i])
            i -= 1
        if j >= 0:
            total_sum += int(b[j])
            j -= 1
            
        result = str(total_sum % 2) + result
        carry = total_sum // 2
        
    return result

# Example usage:
a = "1010"
b = "1011"
print(addBinary(a, b))  # Output: "10101"
