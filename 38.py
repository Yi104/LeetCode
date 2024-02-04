def countAndSay(n):
    if n == 1:
        return "1"
    
    prev_result = countAndSay(n - 1)
    result = ""
    count = 1
    
    for i in range(len(prev_result)):
        if i + 1 < len(prev_result) and prev_result[i] == prev_result[i + 1]:
            count += 1
        else:
            result += str(count) + prev_result[i]
            count = 1
    
    return result

# Example usage:
n = 4
result = countAndSay(n)
print(result)
