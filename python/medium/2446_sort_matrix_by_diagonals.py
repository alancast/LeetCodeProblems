from typing import List


class Solution:
    # Go over diagonals, create temp array, sort temp array then edit in place
    # Time O(n * nlogn)
    # Space O(n)
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # Do bottom left triangle diagonals
        for row_index in range(n):
            temp_array = []

            # Fill in temp array
            col_index = 0
            temp_row = row_index
            while temp_row < n:
                temp_array.append(grid[temp_row][col_index])
                temp_row += 1
                col_index += 1

            # Sort temp array
            temp_array.sort(reverse=True)

            # Replace grid entries
            col_index = 0
            temp_row = row_index
            while temp_row < n:
                grid[temp_row][col_index] = temp_array[col_index]
                temp_row += 1
                col_index += 1
        
        # Do top right triangle diagonals
        for col_index in range(1, n):
            temp_array = []

            # Fill in temp array
            row_index = 0
            temp_col = col_index
            while temp_col < n:
                temp_array.append(grid[row_index][temp_col])
                temp_col += 1
                row_index += 1

            # Sort temp array
            temp_array.sort()

            # Replace grid entries
            row_index = 0
            temp_col = col_index
            while temp_col < n:
                grid[row_index][temp_col] = temp_array[row_index]
                temp_col += 1
                row_index += 1

        return grid

test_cases = [
    [[[8,2,3],[9,6,7],[4,5,1]], [[1,7,3],[9,8,2],[4,5,6]]],
    [[[2,1],[1,0]], [[0,1],[1,2]]],
    [[[1]], [[1]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.sortMatrix(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")