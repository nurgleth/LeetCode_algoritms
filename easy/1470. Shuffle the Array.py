"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].



Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
"""


def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    listed = []
    for i in range(n):
        listed.append(nums[i])
        listed.append(nums[i + n])
    print(listed)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    shuffle(nums, n)

    nums1 = [2, 5, 1, 3, 4, 7]
    n1 = 3
    shuffle(nums1, n1)

    nums2 = [1, 1, 2, 2]
    n2 = 2
    shuffle(nums2, n2)
