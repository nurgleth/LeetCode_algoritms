"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j] and i < j:
                num+=1
    return num


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    numIdenticalPairs(nums)

    nums1 = [1, 1, 1, 1]
    numIdenticalPairs(nums1)

    nums2 = [1, 2, 3]
    numIdenticalPairs(nums2)
