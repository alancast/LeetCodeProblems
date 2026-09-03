from collections import deque


class Solution:
    # BFS with bitmasking to keep track of which students have been cleaned
    # Time O(m * n * 2^k) where k is the number of students
    # Space O(m * n * 2^k)
    def minMoves(self, classroom: list[str], energy: int) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        m = len(classroom)
        n = len(classroom[0])

        id = [[0] * n for _ in range(m)]

        # Find starting point as well as how much litter needs cleaned
        start_x = start_y = 0
        count = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start_x, start_y = i, j
                elif classroom[i][j] == "L":
                    id[i][j] = 1 << count
                    count += 1

        full = 1 << count
        bestEnergy = [
            [[-1 for _ in range(full)] for _ in range(n)] for _ in range(m)
        ]
        bestEnergy[start_x][start_y][0] = energy

        # Do BFS with queue, keeping track of x, y, mask of cleaned students, energy left, and steps taken
        queue = deque()
        queue.append((start_x, start_y, 0, energy, 0))
        while queue:
            x, y, mask, ener, steps = queue.popleft()
            # See if we have cleaned everything
            if mask == full - 1:
                return steps

            # We have no energy so can't move
            if ener == 0:
                continue

            # Add all adjacent squares that are valid
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # Make sure next square is within bounds and can be moved to
                if (
                    nx < 0
                    or nx >= m
                    or ny < 0
                    or ny >= n
                    or classroom[nx][ny] == "X"
                ):
                    continue

                # If next square is reset square max out energy, otherwise subtract 1
                next_energy = energy if classroom[nx][ny] == "R" else ener - 1

                nmask = mask | id[nx][ny]
                # If we have a higher energy than when we've visited this square before, update best energy
                # And append next square to the queue to evaluate
                if next_energy > bestEnergy[nx][ny][nmask]:
                    bestEnergy[nx][ny][nmask] = next_energy
                    queue.append((nx, ny, nmask, next_energy, steps + 1))

        # We couldn't clean everything and did full search, so return -1
        return -1

test_cases = [
    [2, ["S.", "XL"], 2],
    [3, ["LS", "RL"], 4],
    [-1, ["L.S", "RXL"], 3]
]
solution = Solution()
for expected, classroom, energy in test_cases:
    actual = solution.minMoves(classroom, energy)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: classroom: {classroom}, energy: {energy}")

print("Ran all tests")
