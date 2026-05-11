class Solution:
    # Math trick basically
    # Reverse on the diagonal then reverse on left to right
    # Time O(n^2) n by n matrix so going over each cell is n^2
    # Space O(1)
    def rotate(self, matrix: list[list[int]]) -> None:
        self.swap_diagonally(matrix)
        self.reverse_left_right(matrix)

    # Swap across the diagonal
    # Time O(n^2)
    # Space O(1)
    def swap_diagonally(self, matrix):
        n = len(matrix)

        # Swap across the diagonal
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse left and right
    # Time O(n^2)
    # Space O(1)
    def reverse_left_right(self, matrix):
        n = len(matrix)

        # Reverse left and right
        for i in range(n):
            # Only need to go to n//2 because swapping
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = (
                    matrix[i][-j - 1],
                    matrix[i][j],
                )

test_cases = [
    [[[7,4,1],[8,5,2],[9,6,3]], [[1,2,3],[4,5,6],[7,8,9]]],
    [[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]]
]
solution = Solution()
for expected, matrix in test_cases:
    solution.rotate(matrix)
    if expected != matrix:
        print(f"FAILED TEST! Expected {expected} but got {matrix}. INPUTS: matrix: {matrix}")

print("Ran all tests")
