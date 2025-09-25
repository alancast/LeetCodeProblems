from typing import List


class Solution:
    # Start at the end and modify array in place then take top
    # At each step add min to row above
    # Time O(n^2)
    # Space O(1)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for row in range(n-1, 0, -1):
            for col in range(row):
                if triangle[row][col] < triangle[row][col+1]:
                    triangle[row-1][col] += triangle[row][col]
                else:
                    triangle[row-1][col] += triangle[row][col+1]

        return triangle[0][0]

test_cases = [
    [11, [[2],[3,4],[6,5,7],[4,1,8,3]]],
    [-10, [[-10]]]
]
solution = Solution()
for expected, triangle in test_cases:
    actual = solution.minimumTotal(triangle)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: triangle: {triangle}")

print("Ran all tests")