from typing import List


class Solution:
    # Prefix sum array
    # Time O(n^2)
    # Space O(n^2)
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Create prefix sum array (n+1 for bound checking)
        prefix_sum_matrix = [[0] * (n + 1) for _ in range(n + 1)]

        # Process queries
        for row1, col1, row2, col2 in queries:
            # Increment upper left corner
            prefix_sum_matrix[row1][col1] += 1

            # Decrement right and down
            prefix_sum_matrix[row1][col2 + 1] -= 1
            prefix_sum_matrix[row2 + 1][col1] -= 1

            # Re-increment after bottom right corner
            prefix_sum_matrix[row2 + 1][col2 + 1] += 1

        # Build answer matrix
        answer = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # Get bounds below, left, and lower left
                x1 = 0 if i == 0 else answer[i - 1][j]
                x2 = 0 if j == 0 else answer[i][j - 1]
                x3 = 0 if i == 0 or j == 0 else answer[i - 1][j - 1]

                # Matrix is prefix sum plus (and minus) prefixes
                answer[i][j] = prefix_sum_matrix[i][j] + x1 + x2 - x3

        return answer

test_cases = [
    [[[1,1,0],[1,2,1],[0,1,1]], 3, [[1,1,2,2],[0,0,1,1]]],
    [[[1,1],[1,1]], 2, [[0,0,1,1]]]
]
solution = Solution()
for expected, n, queries in test_cases:
    actual = solution.rangeAddQueries(n, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, queries: {queries}")

print("Ran all tests")