class Solution:
    # DP solution
    # Track paths entering each cell from above or from the left.
    # Time O(mn)
    # Space O(n)
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        rows = len(grid)
        cols = len(grid[0])

        # Store paths arriving from above and from the left for each column.
        paths = [[0, 0] for _ in range(cols)]
        paths[0][0] = 1

        # Update each cell using the paths reaching it from the previous row and column.
        for row in range(rows):
            for col in range(cols):
                if row > 0:
                    # An empty cell keeps both incoming directions; a mirror only reflects paths from the left downward.
                    if grid[row - 1][col] == 0:
                        paths[col][0] = (paths[col][0] + paths[col][1]) % MOD
                    else:
                        paths[col][0] = paths[col][1]

                if col > 0:
                    # An empty cell keeps both incoming directions; a mirror only reflects paths from above to the right.
                    if grid[row][col - 1] == 0:
                        paths[col][1] = (paths[col - 1][0] + paths[col - 1][1]) % MOD
                    else:
                        paths[col][1] = paths[col - 1][0]

        # The destination can be reached from above or from the left.
        return (paths[-1][0] + paths[-1][1]) % MOD

test_cases = [
    [5, [[0,1,0],[0,0,1],[1,0,0]]],
    [2, [[0,0],[0,0]]],
    [1, [[0,1,1],[1,1,0]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.uniquePaths(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
