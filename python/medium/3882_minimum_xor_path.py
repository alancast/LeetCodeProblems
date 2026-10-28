class Solution:
    # DP solution
    # Time O(mnV)
    # Space O(nV)
    def minCost(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [set() for _ in range(cols)]
        dp[0].add(grid[0][0])

        # Go over each cell and see if reachable
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                reachable = dp[j] | (dp[j - 1] if j > 0 else set())

                dp[j] = {k ^ value for k in reachable}

        # Return min cost at end of grid
        return min(dp[-1])

test_cases = [
    [6, [[1,2],[3,4]]],
    [9, [[6,7],[5,8]]],
    [0, [[2,7,5]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.minCost(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
