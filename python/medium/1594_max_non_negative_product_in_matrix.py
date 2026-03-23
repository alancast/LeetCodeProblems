class Solution:
    MOD = 10**9 + 7

    # Just keep track of previous row and at each index see what max is
    # Time O(mn)
    # Space O(cols)
    def maxProductPath(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # See if start or end is 0
        if grid[0][0] == 0 or grid[rows-1][cols-1] == 0:
            return 0

        # Stores a tuple of (min, max)
        prev_row = []
        # Compute first row
        product = 1
        for col in range(cols):
            product *= grid[0][col]
            prev_row.append((product, product))

        for row in range(1, rows):
            curr_row = []
            for col in range(cols):
                curr_num = grid[row][col]

                # If col is 0 must come from top
                if col == 0:
                    curr_row.append((curr_num * prev_row[0][0], curr_num * prev_row[0][1]))
                    continue

                # Compute four possibles
                from_top_min = prev_row[col][0] * curr_num
                from_top_max = prev_row[col][1] * curr_num
                from_left_min = curr_row[-1][0] * curr_num
                from_left_max = curr_row[-1][1] * curr_num

                # Store best min and max
                min_val = min(from_top_min, from_top_max, from_left_min, from_left_max)
                max_val = max(from_top_min, from_top_max, from_left_min, from_left_max)
                curr_row.append((min_val, max_val))

            prev_row = curr_row

        if prev_row[-1][1] < 0:
            return -1

        return prev_row[-1][1] % self.MOD

test_cases = [
    [-1, [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]],
    [8, [[1,-2,1],[1,-2,1],[3,-4,1]]],
    [0, [[1,3],[0,-4]]],
    [0, [[-1,3,0],[3,-2,3],[-1,1,-4]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.maxProductPath(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
