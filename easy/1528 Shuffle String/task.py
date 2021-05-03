"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Constraints:

s.length == indices.length == n
1 <= n <= 100
s contains only lower-case English letters.
0 <= indices[i] < n
All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).
"""


def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    dicted = {}
    string = ""
    for i, j in zip(indices, s):
        dicted[i] = j
    for key in sorted(dicted.keys()):
        string += dicted[key]
    return string


def restoreString1(s: str, indices: list[int]) -> str:  # решение и без сортировки
    m = {}
    for i, j in zip(s, indices):
        m[j] = i
    out = ""
    for i in range(len(s)):
        out += m[i]
    return out
