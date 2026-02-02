from collections import deque
from typing import List


class Solution:
    # Problem defined constant for empty room
    EMPTY_ROOM = 2147483647

    # BFS from all gates to all options
    # Time O(m*n)
    # Space O(m*n)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        gate = 0

        # Add all the gates to a queue to process
        rows = len(rooms)
        cols = len(rooms[0])
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == gate:
                    q.append([row, col])

        # Process from queue of all gates to what squares they can go to
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        distance = 0
        while q:
            size = len(q)
            distance += 1

            # Go over every cell in the queue and process it's neighbors
            while size > 0:
                # How we keep track of making sure we process just this iteration
                size -= 1
                row, col = q.popleft()

                # Go in all different dirs
                for dx, dy in dirs:
                    next_row = row + dx
                    next_col = col + dy
                    # Make sure next cell is in bounds and is empty room we haven't been to
                    # As soon as we go there we have the min distance to there
                    # So eventually there will be no unvisited empty rooms left
                    if (0 <= next_row < rows and 
                        0 <= next_col < cols and 
                        rooms[next_row][next_col] == self.EMPTY_ROOM):
                        rooms[next_row][next_col] = distance
                        q.append([next_row, next_col])
