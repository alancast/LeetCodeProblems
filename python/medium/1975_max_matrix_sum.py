from typing import List


class Solution:
    # If it's an even number of negative numbers you can make all positive
    # If odd number, just pick smallest number and subtract that
    # So go over whole matrix and track and sum
    # Time O(n^2) just go over each cell once
    # Space O(1)
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        abs_sum = num_neg = 0
        smallest_abs = float('inf')

        # Go over all the values in the matrix
        for row in range(n):
            for col in range(n):
                num = matrix[row][col]

                # See how many negative numbers total
                if num < 0:
                    num_neg += 1

                # Update sum and see if new smallest num
                num = abs(num)
                abs_sum += num
                smallest_abs = min(smallest_abs, num)

        # See if even or odd num of negative numbers
        if num_neg % 2 == 0:
            return abs_sum
        else:
            # Must subtract it twice because it was initially added
            return abs_sum - (2 * int(smallest_abs))

test_cases = [
    [4, [[1,-1],[-1,1]]],
    [16, [[1,2,3],[-1,-2,-3],[1,2,3]]]
]
solution = Solution()
for expected, matrix in test_cases:
    actual = solution.maxMatrixSum(matrix)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: matrix: {matrix}")

print("Ran all tests")
