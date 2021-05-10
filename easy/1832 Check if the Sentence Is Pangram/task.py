"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""


def checkIfPangram(sentence: str) -> bool:
    return len(set(sentence)) == 26
