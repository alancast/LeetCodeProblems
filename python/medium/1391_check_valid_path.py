from collections import deque


class DisjointSet:
    def __init__(self, n):
        self.set = list(range(n))

    def find(self, x):
        if x == self.set[x]:
            return x

        self.set[x] = self.find(self.set[x])
        return self.set[x]

    def merge(self, x, y):
        self.set[self.find(x)] = self.find(y)


class Solution:
    # Just follow the path
    # Keep track of visited
    # This problem is stupid
    # Time O(mn)
    # Space O(mn)
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        # Init
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        # Init bfs queue
        queue = deque([(0, 0)])
        visited = {(0, 0)}

        while queue:
            r, c = queue.popleft()
            # Check if we are at end
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc

                # Check bounds
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:  # noqa: SIM102
                    # Check if neighbor can connect back to current
                    # neighbor must have direction which is negative of (dr, dc)
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        # Nothing left to visit and never got to end
        return False

    # Just follow the path
    # Keep track of visited and what direction you came from
    # Code would be unnecessarily ugly. This problem is stupid
    # Instead just do disjoint set and see if they are the same set at the end
    # Time O(mn)
    # Space O(mn)
    def hasValidPath_disjoint_set(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        ds = DisjointSet(m * n)

        def getId(x, y):
            return x * n + y

        def detectL(x, y):
            if y - 1 >= 0 and grid[x][y - 1] in [1, 4, 6]:
                ds.merge(getId(x, y), getId(x, y - 1))

        def detectR(x, y):
            if y + 1 < n and grid[x][y + 1] in [1, 3, 5]:
                ds.merge(getId(x, y), getId(x, y + 1))

        def detectU(x, y):
            if x - 1 >= 0 and grid[x - 1][y] in [2, 3, 4]:
                ds.merge(getId(x, y), getId(x - 1, y))

        def detectD(x, y):
            if x + 1 < m and grid[x + 1][y] in [2, 5, 6]:
                ds.merge(getId(x, y), getId(x + 1, y))

        def handler(x, y):
            if grid[x][y] == 1:
                detectL(x, y)
                detectR(x, y)
            elif grid[x][y] == 2:  # noqa: PLR2004
                detectU(x, y)
                detectD(x, y)
            elif grid[x][y] == 3:  # noqa: PLR2004
                detectL(x, y)
                detectD(x, y)
            elif grid[x][y] == 4:  # noqa: PLR2004
                detectR(x, y)
                detectD(x, y)
            elif grid[x][y] == 5:  # noqa: PLR2004
                detectL(x, y)
                detectU(x, y)
            else:
                detectR(x, y)
                detectU(x, y)

        # Handle every square
        for i in range(m):
            for j in range(n):
                handler(i, j)

        # See if start and end are in same set, if so there is a path
        return ds.find(getId(0, 0)) == ds.find(getId(m - 1, n - 1))

test_cases = [
    [True, [[2,4,3],[6,5,2]]],
    [False, [[1,2,1],[1,2,1]]],
    [False, [[1,1,2]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.hasValidPath(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
