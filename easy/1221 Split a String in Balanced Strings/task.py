"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Constraints:

1 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.
"""


def balancedStringSplit(s: str) -> int:
    tmp_R = 0
    tmp_L = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] == "R":
            tmp_R += 1
            if tmp_R == tmp_L:
                tmp += 1
        elif s[i] == "L":
            tmp_L += 1
            if tmp_R == tmp_L:
                tmp += 1
    return tmp

def balancedStringSplit1(s: str) -> int:
    count = 0
    balance = 0
    for i in s:
        if i == 'R':
            balance += 1
        if i == 'L':
            balance -= 1
        if balance == 0:
            count += 1
    return count
