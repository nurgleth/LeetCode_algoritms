"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""


def arraySign(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 1
    for i in nums:
        a*=i
    if a > 0:
        return 1
    elif a < 0:
        return -1
    return 0

nums = [-1, -2, -3, -4, 3, 2, 1]  # 144
print(arraySign(nums))
