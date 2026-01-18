from typing import List


class Solution:
    # Compute prefix sum of all rows and columns and just check squares
    # Go from large to small, stop as soon as find first one
    # Time O(mn)
    # Space O(mn)
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Prefix sum of each row
        row_sums = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            row_sums[row][0] = grid[row][0]
            for col in range(1, cols):
                row_sums[row][col] = row_sums[row][col - 1] + grid[row][col]

        # Prefix sum of each column
        col_sums = [[0] * cols for _ in range(rows)]
        for col in range(cols):
            col_sums[0][col] = grid[0][col]
            for row in range(1, rows):
                col_sums[row][col] = col_sums[row - 1][col] + grid[row][col]

        # Check all squares starting large and getting smaller
        for side_len in range(min(rows, cols), 1, -1):

            # Check all top-left corner positions (i,j) of the square
            # Goes over whole first row each column then goes to second row
            for row in range(rows - side_len + 1):
                for col in range(cols - side_len + 1):

                    # Can use just first row for target sum (as must all be equal)
                    target_sum = row_sums[row][col + side_len - 1]
                    # Just classic end minus start, but 0 being potential makes this ugly if
                    if col > 0:
                        target_sum -= row_sums[row][col - 1]

                    continue_check = True

                    # Check all the row sums
                    for next_row in range(row + 1, row + side_len):
                        row_sum = row_sums[next_row][col + side_len - 1]
                        # Just classic end minus start, but 0 being potential makes this ugly if
                        if col > 0:
                            row_sum -= row_sums[next_row][col - 1]
                        
                        if row_sum != target_sum:
                            continue_check = False
                            break
                    
                    # If not all the rows have the same sum, no reason to check rest
                    if not continue_check:
                        continue

                    # Check all the col sums
                    for next_col in range(col, col + side_len):
                        col_sum = col_sums[row + side_len - 1][next_col]
                        # Just classic end minus start, but 0 being potential makes this ugly if
                        if row > 0:
                            col_sum -= col_sums[row - 1][next_col]

                        if col_sum != target_sum:
                            continue_check = False
                            break

                    # If not all the cols have the same sum, no reason to check rest
                    if not continue_check:
                        continue

                    # Find sums of diagonals (no prefix sum, just add)
                    d1 = d2 = 0
                    for k in range(side_len):
                        d1 += grid[row + k][col + k]
                        d2 += grid[row + k][col + side_len - 1 - k]

                    # If these also equal target sum we have a winner, otherwise check next
                    if d1 == target_sum and d2 == target_sum:
                        return side_len

        # Any square of 1 is magic, so if no larger ones are found return 1
        return 1

test_cases = [
    [3, [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]],
    [2, [[5,1,3,1],[9,3,3,1],[1,3,3,8]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.largestMagicSquare(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
