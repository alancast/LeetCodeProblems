from typing import List


class Solution:
    # Depth first search to see if destination is reachable
    # Time O(m*n * (m+n))
    # Space O(m*n) for visit array
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        # Keep track of what nodes have been visited thus far
        visit = [[False] * cols for _ in range(rows)]

        # Do a depth first search and see if destination is reachable
        return self._dfs(rows, cols, maze, start, destination, visit)

    def _dfs(
        self,
        rows: int,
        cols: int,
        maze: List[List[int]],
        current_node: List[int],
        destination: List[int],
        visit: List[List[bool]],
    ) -> bool:
        # If we already visited this location don't redo work
        if visit[current_node[0]][current_node[1]]:
            return False
        # If this is the destination we have found a path out!
        if current_node[0] == destination[0] and current_node[1] == destination[1]:
            return True

        # Mark the current node as visited
        visit[current_node[0]][current_node[1]] = True
        dirX = [0, 1, 0, -1]
        dirY = [-1, 0, 1, 0]

        # Go in all directions and add next location to queue
        for i in range(4):
            r = current_node[0]
            c = current_node[1]
            # Move the ball in the chosen direction until it can.
            while r >= 0 and r < rows and c >= 0 and c < cols and maze[r][c] == 0:
                r += dirX[i]
                c += dirY[i]

            # See if this location can lead to exit
            # Subtract the final move that broke the while bound checking (one step too far)
            if self._dfs(rows, cols, maze, [r - dirX[i], c - dirY[i]], destination, visit):
                return True

        # Explored it all and couldn't find path
        return False

test_cases = [
    [True, [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]],
    [False, [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2]],
    [False, [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1]]
]
solution = Solution()
for expected, maze, start, destination in test_cases:
    actual = solution.hasPath(maze, start, destination)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: maze: {maze}, start: {start}, destination: {destination}")

print("Ran all tests")
