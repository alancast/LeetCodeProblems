from typing import List


class Solution:
    # Just go over all point pairs and compute area and save max
    # Time O(n^3)
    # Space O(1)
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)

        max_area = 0
        for i in range(n):
            for j in range(i, n):
                for k in range (j, n):
                    x1 = points[i][0]
                    x2 = points[j][0]
                    x3 = points[k][0]

                    y1 = points[i][1]
                    y2 = points[j][1]
                    y3 = points[k][1]

                    temp_area = abs(0.5 * (x1*(y2-y3) + x2*(y3 - y1) + x3*(y1-y2)))

                    max_area = max(temp_area, max_area)

        return max_area

test_cases = [
    [2.00000, [[0,0],[0,1],[1,0],[0,2],[2,0]]],
    [.50000, [[1,0],[0,0],[0,1]]]
]
solution = Solution()
for expected, points in test_cases:
    actual = solution.largestTriangleArea(points)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: points: {points}")

print("Ran all tests")