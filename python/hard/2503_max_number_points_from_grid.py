from heapq import heappop, heappush
from typing import List


class Solution:
    # Search in sorted query order so search just happens once
    # n is num rows, m is num cols, k is num queries
    # Time O(klogk + n*mlogmn)
    # Space O(nm + k)
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row_count = len(grid)
        col_count = len(grid[0])
        result = [0] * len(queries)
        # Directions for movement (right, down, left, up)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Store queries along with their original indices to restore order later
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        # Min-heap to process cells in increasing order of value
        min_heap = []
        visited = [[False] * col_count for _ in range(row_count)]
        # Keeps track of the number of cells processed
        total_points = 0
        # Start from the top-left cell (heap contains tuple of value, row, col)
        heappush(min_heap, (grid[0][0], 0, 0))
        visited[0][0] = True

        # Process queries in sorted order
        for query_value, query_index in sorted_queries:
            # Expand the cells that are smaller than the current query value
            while min_heap and min_heap[0][0] < query_value:
                _, current_row, current_col = heappop(min_heap)

                # Increment count of valid cells
                total_points += 1

                # Explore all four possible directions
                for row_offset, col_offset in DIRECTIONS:
                    new_row = current_row + row_offset
                    new_col = current_col + col_offset

                    # Check if the new cell is within bounds and not visited
                    if new_row >= 0 and new_col >= 0 and new_row < row_count \
                    and new_col < col_count and not visited[new_row][new_col]:
                        heappush(min_heap,(grid[new_row][new_col], new_row, new_col))
                        # Mark as visited
                        visited[new_row][new_col] = True

            # Store the result for this query
            result[query_index] = total_points

        return result
    
test_cases = [
    [[5,8,1], [[1,2,3],[2,5,7],[3,5,1]], [5,6,2]],
    [[0], [[5,2,1],[1,1,2]], [3]]
]
solution = Solution()
for expected, grid, queries in test_cases:
    actual = solution.maxPoints(grid, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, queries: {queries}")

print("Ran all tests")