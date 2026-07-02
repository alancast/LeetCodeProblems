from collections import deque
from heapq import heappop, heappush


class Solution:
    # Since every cell is valued 0 or 1 we can do BFS instead of djikstras
    # Time O(mn)
    # Space O(mn)
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Create a distance matrix to check health
        dis = [[float("inf")] * n for _ in range(m)]

        # Queue just stores x and y
        q = deque()
        q.appendleft((0, 0))
        dis[0][0] = grid[0][0]

        # Just go over the queue until either end or no neighbors left to add
        while q:
            cx, cy = q.popleft()
            # The first time we see the end that guarantees shortest path
            if cx == m - 1 and cy == n - 1:
                return True

            # Add all neighbors to queue
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                # If neighbor is invalid don't add
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                # Make sure the new distance meets the health requirements
                cost = dis[cx][cy] + grid[nx][ny]
                if cost >= health:
                    continue

                # Add neighbor to queue
                if cost < dis[nx][ny]:
                    dis[nx][ny] = cost
                    if grid[nx][ny] == 0:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))

        # We couldn't get to the end
        return False

    # Djikstras algorithm
    # Time O(mn log(mn))
    # Space O(mn)
    def findSafeWalk_djikstras(self, grid: list[list[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        dis = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Queue is in format (cost, x, y)
        pq = [(grid[0][0], 0, 0)]
        while pq:
            val, cx, cy = heappop(pq)
            # If we can't go there skip it
            if dis[cx][cy] >= 0:
                continue

            dis[cx][cy] = val
            # Add neighbors to queue
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and dis[nx][ny] == -1:
                    # Current value plus grid (if it takes a health hit)
                    heappush(pq, (val + grid[nx][ny], nx, ny))

        # See if the end is viable
        return dis[m - 1][n - 1] < health

test_cases = [
    [True, [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 1],
    [False, [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], 3],
    [True, [[1,1,1],[1,0,1],[1,1,1]], 5]
]
solution = Solution()
for expected, grid, health in test_cases:
    actual = solution.findSafeWalk(grid, health)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, health: {health}")

print("Ran all tests")
