class Solution:
    # DFS
    # Time O(mn)
    # Space O(mn)
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)

        def dfs(i: int, j: int) -> int:
            total = grid[i][j]
            grid[i][j] = 0
            for d in range(4):
                x, y = i + dirs[d], j + dirs[d + 1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    total += dfs(x, y)
            return total

        return sum(
            grid[i][j] > 0 and dfs(i, j) % k == 0
            for i in range(m)
            for j in range(n)
        )

test_cases = [
    [
        2,
        [[0, 2, 1, 0, 0], [0, 5, 0, 0, 5], [0, 0, 1, 0, 0], [0, 1, 4, 7, 0], [0, 2, 0, 0, 8]],
        5,
    ],
    [6, [[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], 3],
]
solution = Solution()
for expected, grid, k in test_cases:
    actual = solution.countIslands(grid, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, k: {k}")

print("Ran all tests")
