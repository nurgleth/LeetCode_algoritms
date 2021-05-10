"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the
ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.



Example 1:

Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color",
ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Constraints:

1 <= items.length <= 104
1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
ruleKey is equal to either "type", "color", or "name".
All strings consist only of lowercase letters.
"""


def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    tmp = 0
    for i in items:
        if ruleKey == "type":
            if i[0] == ruleValue:
                tmp += 1
        elif ruleKey == "color":
            if i[1] == ruleValue:
                tmp += 1
        elif ruleKey == "name":
            if i[2] == ruleValue:
                tmp += 1
        else:
            pass
    return tmp
