from typing import List


class Solution:
    # DP of how many ways to get to square with mod 0
    # Time O(n*m*k)
    # Space O(n*m*k)
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7

        # Initialize DP array with all 0's as originally there are 0 paths
        rows = len(grid)
        cols = len(grid[0])
        dp = [[[0] * k for _ in range(cols + 1)] for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if row == 1 and col == 1:
                    dp[row][col][grid[0][0] % k] = 1
                    continue

                # Go over all possible mods of the previous squares
                value = grid[row - 1][col - 1] % k
                for r in range(k):
                    prev_mod = (r - value + k) % k
                    dp[row][col][r] = (
                        dp[row - 1][col][prev_mod] + dp[row][col - 1][prev_mod]
                    ) % MOD

        # How many ways to get here with no remainder
        return dp[rows][cols][0]

test_cases = [
    [2, [[5,2,4],[3,0,5],[0,7,2]], 3],
    [1, [[0,0]], 5],
    [10, [[7,3,4,9],[2,3,6,2],[2,3,7,0]], 1]
]
solution = Solution()
for expected, grid, k in test_cases:
    actual = solution.numberOfPaths(grid, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, k: {k}")

print("Ran all tests")