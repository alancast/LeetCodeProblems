from collections import deque


class Solution:
    # BFS solution
    # Time O(mn)
    # Space O(mn)
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and self.bfs(i, j, m, n, grid, visit):
                    count += 1

        return count

    def bfs(  # noqa: PLR0913, PLR0917
        self,
        x: int,
        y: int,
        m: int,
        n: int,
        grid: list[list[int]],
        visit: list[list[bool]],
    ) -> bool:
        q = deque([(x, y)])
        visit[x][y] = True
        is_closed = True

        dir_x = [0, 1, 0, -1]
        dir_y = [-1, 0, 1, 0]

        while q:
            x, y = q.popleft()

            for i in range(4):
                r, c = x + dir_x[i], y + dir_y[i]
                if r < 0 or r >= m or c < 0 or c >= n:
                    # (x, y) is a boundary cell.
                    is_closed = False
                elif grid[r][c] == 0 and not visit[r][c]:
                    q.append((r, c))
                    visit[r][c] = True

        return is_closed

test_cases = [
    [2, [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]],
    [1, [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]],
    [2, [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]],
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.closedIsland(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}")

print("Ran all tests")
