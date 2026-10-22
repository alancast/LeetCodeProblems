from collections import deque
from heapq import heappop, heappush


class Solution:
    # Direction vectors for up, down, left, right movement
    _DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # noqa: RUF012

    # Manhattan distance solution. More complicated than simple BFS solution below
    # Faster, but larger potential runtime
    # Time O((mn)^2)
    # Space O(mn)
    def getFood(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        start = []
        foods = []

        # Find starting position and all food locations
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    start = [r, c]
                elif grid[r][c] == "#":
                    foods.append([r, c])

        if not foods:
            return -1

        # Track visited cells to avoid cycles
        seen = set()

        # Priority queue stores: (estimated total cost, steps taken, row, col)
        pq = [(self._calc_dist(start[0], start[1], foods), 0, start[0], start[1])]

        while pq:
            _, steps, r, c = heappop(pq)

            # Try all four directions
            for dr, dc in self._DIRS:
                new_r, new_c = r + dr, c + dc

                if (
                    not self._is_valid(grid, new_r, new_c)
                    or (new_r, new_c) in seen
                ):
                    continue

                # If food found, return total steps taken
                if grid[new_r][new_c] == "#":
                    return steps + 1

                seen.add((new_r, new_c))
                # Calculate new Manhattan distance estimate
                new_est = self._calc_dist(new_r, new_c, foods)
                heappush(
                    pq, (new_est + steps + 1, steps + 1, new_r, new_c)
                )

        return -1

    # Calculate Manhattan distance to nearest food
    def _calc_dist(self, r: int, c: int, foods: list[list[int]]) -> int:
        return min(abs(food[0] - r) + abs(food[1] - c) for food in foods)

    # Check if position is within grid bounds and not an obstacle
    def _is_valid(self, grid: list[list[str]], row: int, col: int) -> bool:
        return (
            0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "X"
        )

    # BFS solution
    # Time O(mn)
    # Space O(mn)
    def getFood_bfs(self, grid: list[list[str]]) -> int:
        # Possible moves: right, left, up, down
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])

        # Find starting position marked as '*'
        start = next(
            (i, j)
            for i in range(rows)
            for j in range(cols)
            if grid[i][j] == "*"
        )

        # BFS queue for level-by-level traversal
        queue = deque([start])
        steps = 1

        # BFS traversal
        while queue:
            # Process all cells at current level
            for _ in range(len(queue)):
                row, col = queue.popleft()

                # Try all four directions
                for dx, dy in dirs:
                    new_row, new_col = row + dx, col + dy

                    if self._is_valid(grid, new_row, new_col):
                        # Found food
                        if grid[new_row][new_col] == "#":
                            return steps

                        # Mark as visited and add to queue
                        grid[new_row][new_col] = "X"
                        queue.append((new_row, new_col))
            steps += 1

        # No path found to food
        return -1

test_cases = [
    [3, [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]],
    [-1, [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]],
    [6, [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]],
    [5, [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["O","O","O","O","O"]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.getFood(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
