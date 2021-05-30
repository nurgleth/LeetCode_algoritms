"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

 Constraints:

points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
"""


def minTimeToVisitAllPoints(points: list[list[int]]) -> int:
    count = 0
    for i in range(len(points) - 1):
        if points[i][0] < points[i + 1][0]:
            tmp_x = [i for i in range(points[i][0], points[i + 1][0])]
        else:
            tmp_x = [i for i in range(points[i + 1][0], points[i][0])]
        if points[i][1] < points[i + 1][1]:
            tmp_y = [i for i in range(points[i][1], points[i + 1][1])]
        else:
            tmp_y = [i for i in range(points[i + 1][1], points[i][1])]
        count += max(len(tmp_x), len(tmp_y))
    return count


def minTimeToVisitAllPoints1(points: list[list[int]]) -> int:
    count = 0
    for i in range(len(points) - 1):
        count += max(abs(points[i + 1][0] - points[i][0]), abs(points[i + 1][1] - points[i][1]))
    return count
