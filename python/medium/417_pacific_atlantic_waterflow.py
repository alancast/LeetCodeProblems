from collections import deque
from typing import List


class Solution:
    # Do BFS from edge of atlantic as well as edge of pacific
    # Find all cells that can be reached from each then answer is intersection of that
    # Time O(mn)
    # Space O(mn)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not heights or not heights[0]: 
            return []
            
        num_rows = len(heights)
        num_cols = len(heights[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = deque()
        atlantic_queue = deque()
        # Add vertical edges
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        # Add horizontal edges
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        
        def bfs(queue: deque) -> set:
            reachable = set()

            # Do BFS
            while queue:
                (row, col) = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))

                # Check all 4 directions
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row = row + x
                    new_col = col + y

                    # Make sure the new cell is within bounds
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue

                    # Make sure the new cell hasn't already been visited
                    if (new_row, new_col) in reachable:
                        continue

                    # Make sure the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if heights[new_row][new_col] < heights[row][col]:
                        continue

                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))

            return reachable
        
        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))

test_cases = [
    [[(0,4),(1,3),(1,4),(2,2),(3,0),(3,1),(4,0)], [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]],
    [[(0,0)], [[1]]]
]
solution = Solution()
for expected, heights in test_cases:
    actual = solution.pacificAtlantic(heights)
    if set(expected) != set(actual):
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: heights: {heights}")

print("Ran all tests")