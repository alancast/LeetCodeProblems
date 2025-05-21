from typing import List


class Solution:
    # The solution below that isn't memory efficient is better imo. But if you need memory here's how
    # Go through whole grid, as soon as you see a 0 set first row and col to it
    # Since we go in order that won't screw up. 
    # Then go through grid and if zero at first spot zero full row/col
    # Special logic around first row to not zero everything
    # Time O(mn)
    # Space O(1)
    def setZeroes_memory_efficient(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_col_needs_zeroed = False
        rows = len(matrix)
        cols = len(matrix[0])

        # Iterate over matrix once for first pass
        for row in range(rows):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            # Otherwise the test case below fails when 0,0 gets set to 0
            if matrix[row][0] == 0:
                first_col_needs_zeroed = True
            for col in range(1, cols):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        # Iterate over the inner matrix once again and using the first row and first column, update the elements.
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0

        # See if the first column needs to be set to zero as well
        if first_col_needs_zeroed:
            for row in range(rows):
                matrix[row][0] = 0

    # Go through whole grid, as soon as you see a 0 add it to a set for row and col
    # Then go through those and zero things out
    # Time O(mn)
    # Space O(m + n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        row_zero_set = set()
        col_zero_set = set()

        # go through once and find zero's
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_zero_set.add(row)
                    col_zero_set.add(col)

        # Go through again and set zero's
        # Set each col
        for col in col_zero_set:
            for i in range(rows):
                matrix[i][col] = 0

        # Set each row
        for row in row_zero_set:
            matrix[row] = [0] * cols

test_cases = [
    [[[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]]
]
solution = Solution()
for expected, matrix in test_cases:
    solution.setZeroes_memory_efficient(matrix)
    if expected != matrix:
        print(f"FAILED TEST! Expected {expected} but got {matrix}. INPUTS: matrix: {matrix}")

print("Ran all tests")