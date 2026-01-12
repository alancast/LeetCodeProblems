from typing import List


class Solution:
    # Just go point by point and do the math
    # Time O(n)
    # Space O(1)
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        last_x = points[0][0]
        last_y = points[0][1]

        for x, y in points:
            # Compute distance to go from last one to this one
            x_dist = abs(x - last_x)
            y_dist = abs(y - last_y)

            # Go diagonal til directly even with one coordinate then straight
            answer += max(x_dist, y_dist)

            last_x = x
            last_y = y

        return answer

test_cases = [
    [7, [[1,1],[3,4],[-1,0]]],
    [5, [[3,2],[-2,2]]]
]
solution = Solution()
for expected, points in test_cases:
    actual = solution.minTimeToVisitAllPoints(points)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: points: {points}")

print("Ran all tests")