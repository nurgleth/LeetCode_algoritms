"""
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.



Example 1:

Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'

Constraints:

1 <= s.length <= 100
s consists only of lowercase English letters and digits.
shift(s[i-1], s[i]) <= 'z' for all odd indices i.
"""


def replaceDigits(s: str) -> str:
    abcd = "abcdefghijklmnopqrstuvwxyz"
    new_str = ""
    for i in range(len(s)):
        tmp = []
        if s[i] in abcd:
            new_str += s[i]
        else:
            tmp.append(s[i])
            new_str += abcd[abcd.find(s[i - 1]) + int(s[i])]
    return new_str


def replaceDigits1(s: str) -> str:
    res = ""
    for char in s:
        if not char.isdigit():
            res += char
        else:
            res += chr(ord(res[-1]) + int(char))
    return res