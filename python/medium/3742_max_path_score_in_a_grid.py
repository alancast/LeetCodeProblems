class Solution:
    # Dynamic programming solution
    # dp[i][j][c] is the maximum score possible to reach cell (i,j) with a total cost of c
    # Time O(mnk)
    # Space O(mnk)
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Start out by making all scores -1 (no path)
        dp = [[[-1] * (k + 1) for _ in range(cols)] for _ in range(rows)]
        dp[0][0][0] = 0

        # Go row by row
        for row in range(rows):
            # Go over each col
            for col in range(cols):
                # Go over all possible costs
                for cost in range(k + 1):
                    if dp[row][col][cost] == -1:
                        continue

                    # Make sure moving down is within bounds and valid
                    if row + 1 < rows:
                        val = grid[row + 1][col]
                        added_cost = 0 if val == 0 else 1
                        if cost + added_cost <= k:
                            dp[row + 1][col][cost + added_cost] = max(
                                dp[row + 1][col][cost + added_cost], dp[row][col][cost] + val
                            )

                    # Make sure moving right is within bounds and valid
                    if col + 1 < cols:
                        val = grid[row][col + 1]
                        added_cost = 0 if val == 0 else 1
                        if cost + added_cost <= k:
                            dp[row][col + 1][cost + added_cost] = max(
                                dp[row][col + 1][cost + added_cost], dp[row][col][cost] + val
                            )

        return max(dp[rows - 1][cols - 1])

test_cases = [
    [2, [[0, 1],[2, 0]], 1],
    [-1, [[0, 1],[1, 2]], 1]
]
solution = Solution()
for expected, grid, k in test_cases:
    actual = solution.maxPathScore(grid, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, k: {k}")

print("Ran all tests")
