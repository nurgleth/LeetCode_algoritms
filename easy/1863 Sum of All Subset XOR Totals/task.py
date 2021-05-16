"""
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Example 1:

Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6

Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20
"""
from itertools import combinations


def subsetXORSum(nums: list[int]) -> int:
    count_max = 0
    count_XOR = 0
    if not len(nums):
        pass
    else:
        for i in nums:
            count_max += i
        if len(nums) > 2:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    count_max += nums[i] ^ nums[j]
        for i in range(len(nums)):
            count_XOR ^= nums[i]

    return count_max + count_XOR


def subsetXORSum1(nums: list[int]) -> int:
    k = []
    for i in range(1, len(nums) + 1):
        k += list(combinations(nums, i))
    sm = 0
    for i in k:
        sm1 = i[0]
        for j in i[1:]:
            sm1 ^= j
        sm += sm1
    return sm
