from heapq import heappop, heappush
from typing import List


class Solution:
    # Dynamic programming 
    # Time O(nlogn) where n is total size of grid
    # Space O(n)
    def minCost(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Create a sorted list of grid spaces for teleportation purposes
        # Each entry will be [cost, row, col]
        sorted_spaces = []
        for row in range(rows):
            for col in range(cols):
                sorted_spaces.append([grid[row][col], row, col])

        # Sort by cost increasing
        sorted_spaces.sort()
        n = len(sorted_spaces)

        # Create cost array for min cost to end from all spots
        costs = [[float("inf")] * cols for _ in range(rows)]

        # Update values for all teleport options
        for _ in range(k + 1):
            minCost = float("inf")
            prev_space_modified = 0

            # Update grid values with teleport knowing we can teleport
            for i in range(n):
                # See if cost from this location is less than all others
                minCost = min(minCost, costs[sorted_spaces[i][1]][sorted_spaces[i][2]])

                # If next space is same value just keep trying to find min cost
                if i + 1 < n and sorted_spaces[i][0] == sorted_spaces[i + 1][0]:
                    i += 1
                    continue

                # The next space has a different cost from the previous ones
                # So go over all previous ones we can teleport to and update their cost
                for r in range(prev_space_modified, i + 1):
                    # Can teleport to this space for free so min cost updated
                    costs[sorted_spaces[r][1]][sorted_spaces[r][2]] = minCost

                # Make sure to update what we last modified
                prev_space_modified = i + 1

            # Go over all squares from end to front and update costs
            # No teleports
            for row in range(rows - 1, -1, -1):
                for col in range(cols - 1, -1, -1):
                    # If the end, cost to get to end from there is 0
                    if row == rows - 1 and col == cols - 1:
                        costs[row][col] = 0
                        continue

                    # If not the last row, update costs upwards
                    if row != rows - 1:
                        costs[row][col] = min(
                            costs[row][col], costs[row + 1][col] + grid[row + 1][col]
                        )
                    # If not the last col, update costs leftward
                    if col != cols - 1:
                        costs[row][col] = min(
                            costs[row][col], costs[row][col + 1] + grid[row][col + 1]
                        )

        # Answer is min cost to reach end from start
        return int(costs[0][0])

    # This will exceed time limit
    # Djikstras and at every move add right and left (if not visited)
    # As well as teleport to all squares less
    # Time O(nlogn) where n is total size of grid
    # Space O(n)
    def minCost_djikstras(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Create a sorted list of grid spaces for teleportation purposes
        # Each entry will be [cost, row, col]
        sorted_spaces = []
        for row in range(rows):
            for col in range(cols):
                sorted_spaces.append([grid[row][col], row, col])

        # Sort by cost increasing
        sorted_spaces.sort()

        # Keep track of what row, col, tel left combos have been visited
        visited = set()

        # Go over sorted spaces and see what teleport options are left
        # Returns list of row col pairs that are viable
        def get_tel_options(grid_val: int) -> List[List[int]]:
            spaces = []

            # Teleport to all possible spaces
            # Efficiency improvements possible here pruning but complicated
            for space_cost, space_row, space_col in sorted_spaces:
                # Only consider spaces with equal or lesser value
                if space_cost > grid_val:
                    break

                spaces.append([space_row, space_col])

            return spaces

        # In the min heap we store (total cost, row, col, teleports left)
        min_heap = [(0, 0, 0, k)]

        # Do djikstras
        while min_heap:
            cost, row, col, tel_left = heappop(min_heap)

            # See if we've already been there with less cost and same tel left
            if (row, col, tel_left) in visited:
                continue

            # Add this to visited
            visited.add((row, col, tel_left))

            # See if at end
            if row == rows - 1 and col == cols - 1:
                return cost
            
            # Add to djikstras below and to the right
            # Below
            if row < rows - 1:
                heappush(min_heap, (cost + grid[row+1][col], row+1, col, tel_left))
            # Right
            if col < cols - 1:
                heappush(min_heap, (cost + grid[row][col+1], row, col+1, tel_left))

            # Add to djikstras all teleportations
            if tel_left > 0:
                for next_row, next_col in get_tel_options(grid[row][col]):
                    heappush(min_heap, (cost, next_row, next_col, tel_left - 1))

        # We will never get here because it's always possible to get to end
        return 0

test_cases = [
    [7, [[1,3,3],[2,5,4],[4,3,5]], 2],
    [9, [[1,2],[2,3],[3,4]], 1]
]
solution = Solution()
for expected, grid, k in test_cases:
    actual = solution.minCost(grid, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, k: {k}")

print("Ran all tests")
