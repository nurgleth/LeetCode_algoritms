"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".



Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""


def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    count = 0
    for i in jewels:
        for j in stones:
            if i is j:
                count += 1
    return count


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    numJewelsInStones(jewels, stones)

    jewels1 = "z"
    stones1 = "ZZ"
    numJewelsInStones(jewels1, stones1)
