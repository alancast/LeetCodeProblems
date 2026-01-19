from typing import List


class Solution:
    # Optimized version with better prefix sum calculation
    # Can compute prefix sum and then in O(1) compute square sum
    # Then go over top left corners and see how big of a square meets criteria
    # And go until no longer any exist
    # Time O(mn)
    # Space O(mn)
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # Compute prefix sum of matrix
        rows = len(mat)
        cols = len(mat[0])
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                prefix_sum[row][col] = (
                    prefix_sum[row - 1][col]
                    + prefix_sum[row][col - 1]
                    - prefix_sum[row - 1][col - 1]
                    + mat[row - 1][col - 1]
                )

        def get_rectangle_sum(x1: int, y1: int, x2: int, y2: int) -> int:
            # Start with full lower right
            rect_sum = prefix_sum[x2][y2]
            # Subtract all rows above starting row
            rect_sum -= prefix_sum[x1 - 1][y2]
            # Subtract all cols before starting col
            rect_sum -= prefix_sum[x2][y1 - 1]
            # Upper left col subtracted twice so add that back in
            rect_sum += prefix_sum[x1-1][y1-1]
            return rect_sum

        upper_bound = min(rows, cols)
        answer = 0
        # Go over all upper left starting points and see how big of square can make
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                # No point in checking smaller side lengths than we already know an answer exists for
                for side_len in range(answer + 1, upper_bound + 1):
                    # See if this side len with this upper left is valid answer
                    if (
                        row + side_len - 1 <= rows
                        and col + side_len - 1 <= cols
                        and get_rectangle_sum(row, col, row + side_len - 1, col + side_len - 1) <= threshold
                    ):
                        answer += 1
                    # If it's not, then nothing bigger will be so break out of loop
                    else:
                        break

        # Got out of loop, return final answer
        return answer

    # Compute row prefix sums then try all squares from big to small
    # Time O(mn)
    # Space O(mn)
    def maxSideLength_prefix_sum_rows(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])

        # Compute row prefix sums
        row_sums = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            row_sums[row][0] = mat[row][0]
            for col in range(1, cols):
                row_sums[row][col] = row_sums[row][col-1] + mat[row][col]

        upper_bound = min(rows, cols)
        # Try progressively shorter side lengths until square below threshold
        for side_len in range(upper_bound, -1, -1):
            # Pick an upper left and compute sum
            for row in range(rows - side_len + 1):
                for col in range(cols - side_len + 1):
                    # Add up row sums
                    square_sum = 0
                    for i in range(side_len):
                        row_sum = row_sums[row + i][col + side_len - 1]
                        if col >= 1:
                            row_sum -= row_sums[row + i][col - 1]

                        square_sum += row_sum

                    # See if we have a winner
                    if square_sum <= threshold:
                        return side_len

        # No square existed below threshold
        return 0

test_cases = [
    [2, [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4],
    [0, [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1]
]
solution = Solution()
for expected, mat, threshold in test_cases:
    actual = solution.maxSideLength(mat, threshold)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: mat: {mat}, threshold: {threshold}")

print("Ran all tests")
