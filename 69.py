def mySqrt(x):
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid
    
    return right
