from collections import defaultdict


class Solution:
    # Keep a dictionary of what numbers we've seen, as well as total sum
    # After each row, check if removal is possible
    # Then do it again vertically, after each column
    # Time O(mn)
    # Space O(mn)
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:  # noqa: PLR0911, PLR0912
        rows = len(grid)
        cols = len(grid[0])

        sum = 0
        # Counts for how many times a number is left below, above, left or right
        bottom_counts = defaultdict(int)
        top_counts = defaultdict(int)
        left_counts = defaultdict(int)
        right_counts = defaultdict(int)

        # Initialize bottom and right maps and find total sum
        for row in grid:
            for x in row:
                sum += x
                bottom_counts[x] += 1
                right_counts[x] += 1

        sum_top = 0
        # Attempt all horizontal cuts
        for row in range(rows - 1):
            for col in range(cols):
                entry = grid[row][col]
                sum_top += entry

                top_counts[entry] += 1
                bottom_counts[entry] -= 1

            # Check if now that row is finished a horizontal cut exists
            sumBottom = sum - sum_top

            if sum_top == sumBottom:
                return True

            diff = abs(sum_top - sumBottom)

            # See if possible by removing from above
            if sum_top > sumBottom:
                if self.check_valid_removal(top_counts, grid, 0, row, 0, cols - 1, diff):
                    return True
            # See if possible by removing from below
            elif self.check_valid_removal(bottom_counts, grid, row + 1, rows - 1, 0, cols - 1, diff):
                return True

        sum_left = 0
        # Attempt all vertical cuts
        for col in range(cols - 1):
            for row in range(rows):
                entry = grid[row][col]
                sum_left += entry

                left_counts[entry] += 1
                right_counts[entry] -= 1

            # Check if now that col is finished a vertical cut exists
            sum_right = sum - sum_left

            if sum_left == sum_right:
                return True

            diff = abs(sum_left - sum_right)

            # See if possible by removing from left
            if sum_left > sum_right:
                if self.check_valid_removal(left_counts, grid, 0, rows - 1, 0, col, diff):
                    return True
            # See if possible by removing from right
            elif self.check_valid_removal(right_counts, grid, 0, rows - 1, col + 1, cols - 1, diff):
                return True

        return False

    # See if it's possible to remove a number but still keep everything connected
    # Time O(1)
    def check_valid_removal(  # noqa: PLR0913
        self,
        map: defaultdict,
        grid: list[list[int]],
        top_row: int,
        bottom_row: int,
        left_col: int,
        right_col: int,
        diff: int,
    ) -> bool:
        row_count = bottom_row - top_row + 1
        col_count = right_col - left_col + 1

        # Single cell
        if row_count * col_count == 1:
            return False

        # 1D row so must be on edge to remove and stay connected
        if row_count == 1:
            return grid[top_row][left_col] == diff or grid[top_row][right_col] == diff

        # 1D column so must be on edge to remove and stay connected
        if col_count == 1:
            return grid[top_row][left_col] == diff or grid[bottom_row][left_col] == diff

        # 2D grid so if diff is in there just remove it and good to go
        return map[diff] > 0

test_cases = [
    [True, [[1,4],[2,3]]],
    [True, [[1,3],[2,4]]],
    [False, [[1,2,4],[2,3,5]]],
    [False, [[4,1,8],[3,2,6]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.canPartitionGrid(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
