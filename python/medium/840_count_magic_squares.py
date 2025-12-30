from typing import List


class Solution:
    # Check each upper left starting point
    # Do some pruning to optimize
    # Time O(m*n)
    # Space O(1)
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def is_magic(row: int, col: int) -> bool:
            # quick prune: center must be 5 in 1..9 magic square
            if grid[row + 1][col + 1] != 5:
                return False

            # Set of what numbers seen so that we make sure all are unique
            seen = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    grid_num = grid[i][j]
                    # Can't have duplicates (or numbers outside of range)
                    if grid_num < 1 or grid_num > 9 or grid_num in seen:
                        return False

                    seen.add(grid_num)

            # Find the sum of the first row
            target_sum = sum(grid[row][col:col + 3])
            # Make sure second and third rows also sum to that
            if sum(grid[row + 1][col:col + 3]) != target_sum \
                or sum(grid[row + 2][col:col + 3]) != target_sum:
                return False

            # Make sure all the columns sum to this as well
            if (grid[row][col] + grid[row + 1][col] + grid[row + 2][col]) != target_sum:
                return False
            if (grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]) != target_sum:
                return False
            if (grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]) != target_sum:
                return False

            # Make sure the diagonals all sum up too
            if (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]) != target_sum:
                return False
            if (grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]) != target_sum:
                return False

            return True

        answer = 0
        # Go over all starting points and see if it is upper left of magic square
        for row in range(rows - 2):
            for col in range(cols - 2):
                if is_magic(row, col):
                    answer += 1

        return answer

test_cases = [
    [1, [[4,3,8,4],[9,5,1,9],[2,7,6,2]]],
    [0, [[8]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.numMagicSquaresInside(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
