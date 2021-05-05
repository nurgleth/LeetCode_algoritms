"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Constraints:

1 <= n <= 10^5
"""
def subtractProductAndSum(n):
    """
    :type n: int
    :rtype: int
    """
    string = str(n)
    multi = 1
    summa = 0
    for i in string:
        multi *= int(i)
        summa += int(i)
    print(multi)
    return multi - summa
