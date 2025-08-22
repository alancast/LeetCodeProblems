from typing import List


class Solution:
    # Find left, right, top, and bottom. Do math to find area
    # Time O(m*n)
    # Space O(1)
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        left = right = top = bottom = -1

        # Find top-most (set others when we see one)
        for row_index in range(rows):
            for col_index in range(cols):
                if grid[row_index][col_index] == 1:
                    # Set left, right, and bottom for starters for this
                    left = right = col_index
                    # Also set top and bottom
                    top = bottom = row_index
                    # Break because we know we won't find a better top
                    break
            
            if top != -1:
                break
        
        # Find bottom-most (set others when we see one)
        for row_index in range(rows - 1, top, -1):
            bottom_found = False
            for col_index in range(cols):
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
        for col_index in range(left):
            left_found = False
            for row_index in range(rows):
                if grid[row_index][col_index] == 1:
                    # Set left
                    left = col_index
                    left_found = True
                    # Break because we know we won't find a better left
                    break
            
            if left_found:
                break
        
        # Find right-most
        for col_index in range(cols - 1, right, -1):
            right_found = False
            for row_index in range(rows):
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
    [6, [[0,1,0],[1,0,1]]],
    [1, [[1,0],[0,0]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.minimumArea(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")