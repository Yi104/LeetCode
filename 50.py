def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

# Example usage:
x = 2.00000
n = 10
print(myPow(x, n))  # Output: 1024.00000
