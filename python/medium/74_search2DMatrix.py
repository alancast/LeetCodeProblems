from typing import List, Tuple


class Solution:
    def computeMNFromIndex(self, index: int) -> Tuple[int, int]:
        if index == 0:
            return 0, 0
            
        m = (index - 1) // self.N
        n = (index - 1) % self.N
        return m,n

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        self.M = len(matrix)
        self.N = len(matrix[0])
        
        left = 0
        right = self.M * self.N

        while left <= right:
            mid = (left + right) // 2
            row_index, col_index = self.computeMNFromIndex(mid)
            num = matrix[row_index][col_index]
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

testCases = [
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1, True],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60, True],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False]
]
implementation = Solution()
for matrix, target, expected in testCases:
    answer = implementation.searchMatrix(matrix, target)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: matrix: {matrix} target: {target}")