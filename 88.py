def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # Make copies of nums1 and nums2 up to their respective sizes
    nums1_copy = nums1[:m]
    nums2_copy = nums2[:n]

    # Initialize pointers for nums1_copy, nums2_copy, and nums1
    p1 = 0
    p2 = 0
    p = 0

    # Iterate over both lists and merge
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2_copy[p2]:
            nums1[p] = nums1_copy[p1]
            p1 += 1
        else:
            nums1[p] = nums2_copy[p2]
            p2 += 1
        p += 1

    # Copy the remaining elements of nums1_copy or nums2_copy if there are any
    if p1 < m:
        nums1[p:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p:] = nums2_copy[p2:]

# Example usage:
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
