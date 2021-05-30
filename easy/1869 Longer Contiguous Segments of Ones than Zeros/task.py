"""
Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.



Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.

Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
"""


def checkZeroOnes(s: str) -> bool:
    tmp_0, tmp_1 = 0, 0
    max_0, max_1 = 0, 0
    for i in s:
        if i == "1":
            tmp_1 += 1
            tmp_0 = 0
            if max_1 < tmp_1:
                max_1 = tmp_1
        else:
            tmp_0 += 1
            tmp_1 = 0
            if max_0 < tmp_0:
                max_0 = tmp_0
    return max_1 > max_0
