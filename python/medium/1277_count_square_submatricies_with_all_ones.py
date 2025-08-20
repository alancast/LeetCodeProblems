from typing import List


class Solution:
    # Go over all matrix and update values to min of things up and to left
    # Add 1 to that. So if all up and to the left are 1's then this cell is
    # The bottom right corner of a 2 by 2 square
    # If they are all 2's then it's a 3 by 3, and so on
    # If it's already a 0 just continue
    # Time O(n*m)
    # Space O(1) as we just modify the passed in matrix
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
    
        # Go over all cells in the matrix and see what they can be a bottom right corner of
        for row in range(1, rows):
            for col in range(1, cols):
                # If it's a 0 do nothing
                if matrix[row][col] == 0:
                    continue
                
                # If it's a 1, see if it's bottom right corner of larger square
                matrix[row][col] = min(matrix[row-1][col], matrix[row-1][col-1], matrix[row][col-1]) + 1
    
        # Sum up all the values
        answer = 0    
        for row in range(rows):
            for col in range(cols):
                answer += matrix[row][col]
        
        return answer

test_cases = [
    [15, [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
        ]],
    [7, [
        [1,0,1],
        [1,1,0],
        [1,1,0]
        ]]
]
solution = Solution()
for expected, matrix in test_cases:
    actual = solution.countSquares(matrix)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: matrix: {matrix}")

print("Ran all tests")