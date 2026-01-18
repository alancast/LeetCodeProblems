from heapq import heappop, heappush
from typing import List


class Solution:
    # Djikstras algorithm
    # Time O(mnlogmn)
    # Space O(mn)
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0]:
            return -1

        m = len(maze)
        n = len(maze[0])
        visited = set()

        pq = [(0, start[0], start[1])]

        # Djikstras until destination
        while pq:
            dist, x, y = heappop(pq)

            # Got to destination
            if x == destination[0] and y == destination[1]:
                return dist

            # See if already visited then add to visited
            if (x,y) in visited:
                continue
            visited.add((x,y))

            # Move in all directions
            for dx, dy in[[0,1],[0,-1],[1,0],[-1,0]]:
                steps = 0
                new_x = x
                new_y = y

                # Go in this direction until you hit a wall
                while (0 <= new_x + dx < m 
                    and 0 <= new_y + dy < n 
                    and maze[new_x + dx][new_y + dy] != 1):
                    steps += 1
                    new_x += dx
                    new_y += dy

                # If we've already been there no need to re-add
                if (new_x, new_y) in visited:
                    continue

                # Push new entry to queue
                heappush(pq, (steps + dist, new_x, new_y))

        # If there is no path and queue is exhausted
        return -1

test_cases = [
    [12, [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]],
    [-1, [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2]],
    [-1, [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1]]
]
solution = Solution()
for expected, maze, start, destination in test_cases:
    actual = solution.shortestDistance(maze, start, destination)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: maze: {maze}, start: {start}, destination: {destination}")

print("Ran all tests")
