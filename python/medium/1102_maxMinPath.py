import heapq
from typing import List


class Solution:
    # Djikstras where the queue is (gridValue, row, col)
    # Pick the max gridValue every time (negative min in python heappq)
    # Once you reach the final square you know you've passed the lowest number you'll pass
    # So you can return your answer
    # O(n*m*log(nm)) time, O(nm) space
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # 4 directions to a cell's possible neighbors.
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        heap = []
        answer = grid[0][0] 

        # Initalize the status of all the cells as 0 (unvisited).
        visited = [[False] * cols for _ in range(rows)]
                
        # Put the top-left cell to the priority queue and mark it as True (visited).     
        # Notice that we save the negative number of cell's value, thus we can always 
        # pop out the cell with the maximum value using a min-heap data structure.
        heapq.heappush(heap, (-grid[0][0], 0, 0))
        visited[0][0] = True
        
        # While the priority queue is not empty.
        while heap:
            # Pop the cell with the largest value.
            cur_val, cur_row, cur_col = heapq.heappop(heap) 

            # Update the minimum value we have visited so far.
            answer = min(answer, -cur_val)

            # If we reach the bottom-right cell we know our max min and can stop
            if cur_row == rows - 1 and cur_col == cols - 1:
                return answer

            for d_row, d_col in dirs:
                new_row = cur_row + d_row
                new_col = cur_col + d_col

                # Check if the current cell has any in bounds unvisited neighbors.
                if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:   
                    # If so, we put this neighbor to the priority queue and mark it as visited.                
                    heapq.heappush(heap, (-grid[new_row][new_col], new_row, new_col))
                    visited[new_row][new_col] = True
