"""
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even,
you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:

Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.

Constraints:

0 <= num <= 10^6
"""


def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    count = 0
    result = num
    while result > 0:
        if not result % 2:
            count += 1
            result //= 2
        else:
            count += 1
            result -= 1
    return count



