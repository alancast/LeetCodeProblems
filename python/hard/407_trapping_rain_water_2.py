from heapq import heappop, heappush


# Class to store the height and coordinates of a cell in the grid
# Purely just to make it prettier
class Cell:
    height: int
    row: int
    col: int

    def __init__(self, height: int, row: int, col: int):
        self.height = height
        self.row = row
        self.col = col

    # Comparison method for the priority queue (min-heap)
    def __lt__(self, other):
        return self.height < other.height


class Solution:
    # Same exact logic as below, just using built ints and tuples for speed
    # Less verbose, if confused try reading explanation in other function
    # Time O(mnlogmn)
    # Space O(mn)
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        rows = len(heightMap)
        cols = len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        heap = []

        # Push all boundary cells into heap
        for row in range(rows):
            for col in range(cols):
                # Make sure boundary
                if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                    heappush(heap, (heightMap[row][col], row, col))
                    visited[row][col] = True

        trapped_water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Process all cells
        while heap:
            height, x, y = heappop(heap)
            # Check in all directions
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # Make sure cell is within bounds and not already visited then process it
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    # If neighbor is lower, water is trapped
                    trapped_water += max(0, height - heightMap[nx][ny])
                    # Push neighbor with effective height
                    heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    # Mark as visited
                    visited[nx][ny] = True

        # Processed full grid, return answer
        return trapped_water

    # Keep an updated priority queue of boundaries (starts with just the edges)
    # Continually pop lowest boundary and see if it has any lower neighbors
    # If it does water is trapped there, so update water trapped
    # Then update the height of that and make it part of boundary
    # Time O(mnlogmn)
    # Space O(mn)
    def trapRainWater_verbose(self, heightMap: list[list[int]]) -> int:
        rows = len(heightMap)
        cols = len(heightMap[0])

        # Keep track of what cells we've already visited
        visited = [[False] * cols for _ in range(rows)]

        # PQ (min-heap) to process boundary cells in increasing height
        boundary_pq = []

        # Create the initial boundary (the edges)
        # First and last column
        for i in range(rows):
            heappush(boundary_pq, Cell(heightMap[i][0], i, 0))
            visited[i][0] = True
            heappush(boundary_pq, Cell(heightMap[i][cols - 1], i, cols - 1))
            visited[i][cols - 1] = True

        # First and last row (don't worry about double add since marking as visited)
        for i in range(cols):
            heappush(boundary_pq, Cell(heightMap[0][i], 0, i))
            visited[0][i] = True
            heappush(boundary_pq, Cell(heightMap[rows - 1][i], rows - 1, i))
            visited[rows - 1][i] = True

        # Initialize the total water volume to 0
        total_water_volume = 0

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # Process cells in the boundary
        while boundary_pq:
            # Pop the cell with the smallest height from the boundary
            current_cell = heappop(boundary_pq)
            current_row = current_cell.row
            current_col = current_cell.col
            min_boundary_height = current_cell.height

            # Explore all 4 neighboring cells
            for dx, dy in dirs:
                neighbor_row = current_row + dy
                neighbor_col = current_col + dx

                # Make sure neighbor is within bounds and unvisited then process it
                if (
                    self._is_valid_cell(neighbor_row, neighbor_col, rows, cols)
                    and not visited[neighbor_row][neighbor_col]
                ):
                    neighbor_height = heightMap[neighbor_row][neighbor_col]

                    # If the neighbor's height is less than the current boundary height,
                    # water can be trapped so add it to the trapped volume
                    if neighbor_height < min_boundary_height:
                        total_water_volume += (min_boundary_height - neighbor_height)

                    # Push the neighbor into the boundary with updated height (to prevent water leakage)
                    heappush(
                        boundary_pq,
                        Cell(
                            max(neighbor_height, min_boundary_height),
                            neighbor_row,
                            neighbor_col,
                        ),
                    )
                    # Mark neighbor as visited
                    visited[neighbor_row][neighbor_col] = True

        # Return the total amount of trapped water after processing all cells
        return total_water_volume

    # Helper function to check if a cell is valid (within grid bounds)
    def _is_valid_cell(self, row: int, col: int, rows: int, cols: int) -> bool:
        return 0 <= row < rows and 0 <= col < cols

test_cases = [
    [4, [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]],
    [10, [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]]
]
solution = Solution()
for expected, height_map in test_cases:
    actual = solution.trapRainWater(height_map)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: height_map: {height_map}")

print("Ran all tests")
