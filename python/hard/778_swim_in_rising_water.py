from heapq import heappush, heappop
from typing import List


class Solution:
    # Djikstras search basically
    # Time O(n^2logn)
    # Space O(n^2)
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        max_seen = grid[0][0]
        djikstras = [(max_seen, 0, 0)]
        queued = set()
        queued.add((0,0))

        # Add neighbors until we reach spot (n,n)
        while djikstras:
            (value, row, col) = heappop(djikstras)
            max_seen = max(max_seen, value)

            # Check if end state is reached
            if row == n-1 and col == n-1:
                return max_seen

            # Check all 4 directions
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = row + x
                new_col = col + y

                # Make sure the new cell is within bounds
                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
                    continue

                # Make sure the new cell hasn't already been visited
                if (new_row, new_col) in queued:
                    continue

                # Add the new cell to the queue
                heappush(djikstras, (grid[new_row][new_col], new_row, new_col))
                queued.add((new_row, new_col))

test_cases = [
    [3, [[0,2],[1,3]]],
    [16, [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.swimInWater(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")