"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.



Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
"""


def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    tmp_1 = ""
    tmp_2 = ""
    for i in word1:
        tmp_1 += i
    for j in word2:
        tmp_2 += j
    return tmp_1 == tmp_2


def arrayStringsAreEqual1(word1: list[str], word2: list[str]) -> bool:
    return "".join(word1) == "".join(word2)
