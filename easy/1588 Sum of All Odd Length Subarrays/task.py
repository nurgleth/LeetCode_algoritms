"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""


def sumOddLengthSubarrays(arr: list[int]) -> int:
    count = 0
    n = len(arr)
    for i in range(len(arr)):
        for j in range(i, n, 2):
            count += sum(arr[i:j + 1])
    return count





