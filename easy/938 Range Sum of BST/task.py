"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with
a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
"""


def rangeSumBST(root, low: int, high: int) -> int:
    node = root
    queue = []
    queue.append(node)
    total = 0

    while len(queue) > 0:
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        if low <= node.val <= high:
            total += node.val

    return total

