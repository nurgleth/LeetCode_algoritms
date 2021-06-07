"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half
and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice
that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""


def halvesAreAlike(s: str) -> bool:
    tmp_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    tmp_left = 0
    tmp_right = 0
    left_str = s[:len(s) // 2]
    right_str = s[len(s) // 2:]
    for i in left_str:
        if i in tmp_list:
            tmp_left += 1
    for i in right_str:
        if i in tmp_list:
            tmp_right += 1
    return tmp_right == tmp_left

