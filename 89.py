def grayCode(n):
    result = [0]
    for i in range(n):
        result += [x + 2**i for x in reversed(result)]
    return result

# Example usage:
n = 3
print(grayCode(n))
