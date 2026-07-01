from collections import deque
from heapq import heappop, heappush
from typing import ClassVar


class Solution:

    # Directions for moving to neighboring cells: right, left, down, up
    dir: ClassVar[list[tuple[int, int]]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Compute the safeness factor of each cell then be greedy in picking path
    # Time O(n^2*logn)
    # Space O(n^2)
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # Mark thieves as 0 and empty cells as -1, and push thieves to the queue
        multi_source_queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # Push thief coordinates to the queue
                    multi_source_queue.append((i, j))
                    # Mark thief cell with 0
                    grid[i][j] = 0
                else:
                    # Mark empty cell with -1
                    grid[i][j] = -1

        # Calculate safeness factor for each cell using BFS
        while multi_source_queue:
            size = len(multi_source_queue)
            while size > 0:
                curr = multi_source_queue.popleft()
                # Check neighboring cells
                for d in self.dir:
                    di, dj = curr[0] + d[0], curr[1] + d[1]
                    val = grid[curr[0]][curr[1]]
                    # Check if the cell is valid and unvisited
                    if self.isValidCell(grid, di, dj) and grid[di][dj] == -1:
                        # Update safeness factor and push to the queue
                        grid[di][dj] = val + 1
                        multi_source_queue.append((di, dj))
                size -= 1

        # Priority queue to prioritize cells with higher safeness factor
        pq = [[-grid[0][0], 0, 0]] # [maximum_safeness_till_now, x-coordinate, y-coordinate]
        grid[0][0] = -1 # Mark the source cell as visited

        # BFS to find the path with maximum safeness factor
        while pq:
            safeness, i, j = heappop(pq)

            # If reached the destination, return safeness factor
            if i == n - 1 and j == n - 1:
                # Negative because min queue for sorting
                return -safeness

            # Check neighboring cells
            for d in self.dir:
                di, dj = i + d[0], j + d[1]
                # Check if the neighboring cell is valid and unvisited
                if self.isValidCell(grid, di, dj) and grid[di][dj] != -1:
                    heappush(pq, [-min(-safeness, grid[di][dj]), di, dj])
                    grid[di][dj] = -1

        return -1

    # Check if a given cell lies within the grid
    def isValidCell(self, grid, i, j) -> bool:
        n = len(grid)
        return 0 <= i < n and 0 <= j < n

test_cases = [
    [0, [[1,0,0],[0,0,0],[0,0,1]]],
    [2, [[0,0,1],[0,0,0],[0,0,0]]],
    [2, [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.maximumSafenessFactor(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
