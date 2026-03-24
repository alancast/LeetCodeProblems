class Solution:
    NO_X = 1000000

    # Go over matrix row by row and keep x and y count
    # Add when delta is 0
    # Time O(nm)
    # Space O(cols)
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        sum_x = [0] * cols
        sum_y = [0] * cols
        answer = 0

        # Go over full matrix
        for row in range(rows):
            row_xs = 0
            row_ys = 0
            for col in range(cols):
                if grid[row][col] == 'X':
                    row_xs += 1
                elif grid[row][col] == 'Y':
                    row_ys += 1

                # Keep track of total x's and y's submatrix with this lower right has
                sum_x[col] += row_xs
                sum_y[col] += row_ys

                # See if this is a valid submatrix
                if sum_x[col] > 0 and sum_x[col] == sum_y[col]:
                    answer += 1

        return answer

    # Go over matrix row by row and keep delta count
    # Add when delta is 0
    # Ugly code because space optimized, much cleaner if just prefix summing full array
    # Time O(nm)
    # Space O(cols)
    def numberOfSubmatrices_ugly(self, grid: list[list[str]]) -> int:  # noqa: PLR0912, PLR0915
        rows = len(grid)
        cols = len(grid[0])

        # Set up first row
        delta_prev_row = [self.NO_X]
        if grid[0][0] == 'X':
            delta_prev_row[0] = -1
        elif grid[0][0] == 'Y':
            delta_prev_row[0] = 1

        # Count submatrices on first row that qualify
        answer = 0
        for col in range(1, cols):
            if grid[0][col] == 'X':
                if delta_prev_row[-1] == self.NO_X:
                    delta_prev_row.append(-1)
                else:
                    delta_prev_row.append(delta_prev_row[-1] - 1)
            elif grid[0][col] == 'Y':
                if delta_prev_row[-1] == self.NO_X:
                    delta_prev_row.append(1)
                else:
                    delta_prev_row.append(delta_prev_row[-1] + 1)
            else:
                delta_prev_row.append(delta_prev_row[-1])

            answer += delta_prev_row[-1] == 0

        # Count submatrices in all subsequent rows
        for row in range(1, rows):

            # Start delta for the current row (taking into account above)
            delta_curr_row = [self.NO_X]
            if grid[row][0] == 'X':
                delta_curr_row[0] = -1
            elif grid[row][0] == 'Y':
                delta_curr_row[0] = 1
            # See if this straight line is good too
            else:
                answer += delta_prev_row[0] == 0

            answer += delta_curr_row[0] + delta_prev_row[0] == 0

            # Go over all subsequent cols
            for col in range(1, cols):
                if grid[row][col] == 'X':
                    if delta_curr_row[-1] == self.NO_X:
                        delta_curr_row.append(-1)
                    else:
                        delta_curr_row.append(delta_curr_row[-1] - 1)
                elif grid[row][col] == 'Y':
                    if delta_curr_row[-1] == self.NO_X:
                        delta_curr_row.append(1)
                    else:
                        delta_curr_row.append(delta_curr_row[-1] + 1)
                else:
                    delta_curr_row.append(delta_curr_row[-1])

                # Count answers
                if delta_curr_row[col] == self.NO_X:
                    answer += delta_prev_row[col] == 0
                elif delta_prev_row[col] == self.NO_X:
                    answer += delta_curr_row[col] == 0
                else:
                    answer += delta_curr_row[col] + delta_prev_row[col] == 0

            # Combine the rows
            for col in range(cols):
                # They both are no x or y, so carry on
                if delta_prev_row[col] == self.NO_X and delta_curr_row[col] == self.NO_X:
                    continue

                # Used to not have x or y but now does
                if delta_prev_row[col] == self.NO_X and delta_curr_row[col] != self.NO_X:
                    delta_prev_row[col] = delta_curr_row[col]
                # Used to have x or y and no change from this
                elif delta_prev_row[col] != self.NO_X and delta_curr_row[col] == self.NO_X:
                    continue
                else:
                    delta_prev_row[col] += delta_curr_row[col]

        return answer

test_cases = [
    [3, [[".","X","."],["X",".","X"],["Y","Y","."],[".","X","X"]]],
    [3, [["X","Y","."],["Y",".","."]]],
    [0, [["X","X"],["X","Y"]]],
    [0, [[".","."],[".","."]]],
    [1, [[".","."],["Y","X"]]],
    [2, [[".",".","."],[".","X","X"],["Y",".","."],["X",".","."]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.numberOfSubmatrices(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
