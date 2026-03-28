class Solution:
    # Just go over all submatrices and add to array, sort then find min diff
    # Time O(k^2logk * mn)
    # Space O(k^2)
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])

        # Initially set answer to all 0's
        answer = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

        # Go over all subarrays
        for row in range(rows - k + 1):
            for col in range(cols - k + 1):

                # Add every element in this submatrix to a flattened list
                k_grid = []
                for k_row in range(row, row + k):
                    for k_col in range(col, col + k):
                        k_grid.append(grid[k_row][k_col])

                # Sort the list and find the min difference
                k_min = float("inf")
                k_grid.sort()
                for idx in range(1, len(k_grid)):
                    # There is a contingency where the diff must be > 0 to be included
                    if k_grid[idx] == k_grid[idx - 1]:
                        continue

                    k_min = min(k_min, k_grid[idx] - k_grid[idx - 1])

                # Update the min
                if k_min != float("inf"):
                    answer[row][col] = int(k_min)

        return answer

test_cases = [
    [[[2]], [[1,8],[3,-2]], 2],
    [[[0,0]], [[3,-1]], 1],
    [[[1,2]], [[1,-2,3],[2,3,5]], 2]
]
solution = Solution()
for expected, grid, k in test_cases:
    actual = solution.minAbsDiff(grid, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, k: {k}")

print("Ran all tests")
