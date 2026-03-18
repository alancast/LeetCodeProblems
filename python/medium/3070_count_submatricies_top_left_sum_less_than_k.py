class Solution:
    # Keep running tally and go row by row
    # Can do without backtracking if keep a running prefix sum of cols of size n
    # Time O(mn)
    # Space O(1)
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        right = cols
        sum = 0
        count = 0

        # Find ones in first row to set right properly
        for col in range(right):
            if sum + grid[0][col] <= k:
                sum += grid[0][col]
                count += 1
            else:
                right = col
                break

        # Find all submatricies after first row
        for row in range(1, rows):
            col = 0
            while col < right:
                if sum + grid[row][col] <= k:
                    sum += grid[row][col]
                    count += 1
                    col += 1
                # Sum is too high so need to remove numbers and add count
                else:
                    # Make sure right can go further left
                    if right == 0:
                        return count

                    # Subtract rightmost col from row above up til top and try again
                    for del_row in range(row - 1, -1, -1):
                        sum -= grid[del_row][right - 1]

                    # Can't go further right than this in next row
                    right -= 1

        return count

test_cases = [
    [4, [[7,6,3],[6,6,1]], 18],
    [6, [[7,2,9],[1,5,0],[2,6,6]], 20]
]
solution = Solution()
for expected, grid, k in test_cases:
    actual = solution.countSubmatrices(grid, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, k: {k}")

print("Ran all tests")
