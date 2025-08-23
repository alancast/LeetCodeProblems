from typing import List


class Solution:
    # Really stupid problem
    # Only 6 possible partition patterns, so just enumerate all 6
    # Move cuts for all 6 and find min
    # Time O(n^2*m^2)
    # Space O(n*m)
    def minimumSum(self, grid: List[List[int]]) -> int:
        rotated_grid = self._rotate(grid)
        return min(self._solve(grid), self._solve(rotated_grid))
    
    # Rotates the input grid counterclockwise 90 degrees
    def _rotate(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0

        rotated_grid = [[0] * n for _ in range(m)]

        # Rotate the grid
        for i in range(n):
            for j in range(m):
                rotated_grid[m - j - 1][i] = grid[i][j]

        return rotated_grid
    
    # Iterate over all potential break lines and find min answer
    def _solve(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        # Cover the whole grid as initial answer
        answer = rows * cols

        for row_index in range(rows - 1):
            for col_index in range(cols - 1):
                # Find answer for top full width and then two rectangles beneath
                temp_answer = self._minimumArea(grid, 0, row_index, 0, cols - 1)
                temp_answer += self._minimumArea(grid, row_index + 1, rows - 1, 0, col_index)
                temp_answer += self._minimumArea(grid, row_index + 1, rows - 1, col_index + 1, cols - 1)
                
                answer = min(answer, temp_answer)

                # Find answer for bottom full with and two rectangles above
                temp_answer = self._minimumArea(grid, 0, row_index, 0, col_index)
                temp_answer += self._minimumArea(grid, 0, row_index, col_index + 1, cols - 1)
                temp_answer += self._minimumArea(grid, row_index + 1, rows - 1, 0, cols - 1)

                answer = min(answer, temp_answer)

        # Find answer for three horizontal sections (pancake stack)
        for row_index in range(rows - 2):
            for row_index_2 in range(row_index + 1, rows - 1):
                temp_answer = self._minimumArea(grid, 0, row_index, 0, cols - 1)
                temp_answer += self._minimumArea(grid, row_index + 1, row_index_2, 0, cols - 1)
                temp_answer += self._minimumArea(grid, row_index_2 + 1, rows - 1, 0, cols - 1)
                
                answer = min(answer, temp_answer)

        return answer

    # Find the minimum area for 1 rectangle covering all the 1s
    # Set the up, down, left, and right bounds
    # Time O(m*n)
    # Space O(1)
    def _minimumArea(
        self, grid: List[List[int]], top_bound: int, 
        bottom_bound: int, left_bound: int, right_bound: int
    ) -> int:
        rows = len(grid)
        cols = len(grid[0])

        left = right = top = bottom = -1

        # Find top-most (set others when we see one)
        for row_index in range(top_bound, bottom_bound + 1):
            for col_index in range(left_bound, right_bound + 1):
                if grid[row_index][col_index] == 1:
                    # Set left, right, and bottom for starters for this
                    left = right = col_index
                    # Also set top and bottom
                    top = bottom = row_index
                    # Break because we know we won't find a better top
                    break
            
            if top != -1:
                break
        
        # Make sure we found a 1, if not then there are none in this grid section
        if top == -1:
            return float('inf')
        
        # Find bottom-most (set others when we see one)
        for row_index in range(bottom_bound, top, -1):
            bottom_found = False
            for col_index in range(left_bound, right_bound + 1):
                if grid[row_index][col_index] == 1:
                    # See if left or right should be updated as well
                    if col_index < left:
                        left = col_index
                    if col_index > right:
                        right = col_index

                    # Set bottom
                    bottom = row_index
                    bottom_found = True
                    # Break because we know we won't find a better bottom
                    break
            
            if bottom_found:
                break
        
        # Find left-most
        for col_index in range(left_bound, right_bound + 1):
            left_found = False
            for row_index in range(top_bound, bottom_bound + 1):
                if grid[row_index][col_index] == 1:
                    # Set left
                    left = col_index
                    left_found = True
                    # Break because we know we won't find a better left
                    break
            
            if left_found:
                break
        
        # Find right-most
        for col_index in range(right_bound, right, -1):
            right_found = False
            for row_index in range(top_bound, bottom_bound + 1):
                if grid[row_index][col_index] == 1:
                    # Set right
                    right = col_index
                    right_found = True
                    # Break because we know we won't find a better right
                    break
            
            if right_found:
                break

        # Now do calculations and return answer
        return (right - left + 1) * (bottom - top + 1)

test_cases = [
    [5, [[1,0,1],[1,1,1]]],
    [5, [[1,0,1,0],[0,1,0,1]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.minimumSum(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")