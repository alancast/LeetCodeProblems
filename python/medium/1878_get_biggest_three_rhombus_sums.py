# Just a class that keeps the top 3 numbers
class Top3:
    def __init__(self):
        self.top3 = [0, 0, 0]

    # Sees if the new number belongs in the top 3
    def put(self, x: int):
        # See if it's new max
        if x > self.top3[0]:
            self.top3[2] = self.top3[1]
            self.top3[1] = self.top3[0]
            self.top3[0] = x
        # See if it's new second
        elif x != self.top3[0] and x > self.top3[1]:
            self.top3[2] = self.top3[1]
            self.top3[1] = x
        # See if it's new third
        elif x != self.top3[0] and x != self.top3[1] and x > self.top3[2]:
            self.top3[2] = x

    # Returns all of the top 3 that are greater than 0
    def get(self) -> list[int]:
        return [num for num in self.top3 if num != 0]


class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        rows = len(grid)
        cols = len(grid[0])

        # Pad top row and left and right col with all 0's
        down_right_sum = [[0] * (cols+2) for _ in range(rows+1)]
        down_left_sum = [[0] * (cols+2) for _ in range(rows+1)]

        # Compute prefix sums going down right and down left
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                current_grid_value = grid[row-1][col-1]

                down_right_sum[row][col] = down_right_sum[row-1][col-1] + current_grid_value
                # This is counter intuitive, but correct
                # Add [row-1][col-1] because of the padding offsets
                down_left_sum[row][col] = down_left_sum[row-1][col + 1] + current_grid_value

        top3 = Top3()
        # Go over all starting points and lengths and compute sums
        for row in range(rows):
            for col in range(cols):
                # a single cell is also a rhombus
                top3.put(grid[row][col])

                # All rhombus widths (and heights)
                for k in range(row + 2, rows, 2):
                    # Compute upper, down, left, and right x and y
                    ux, uy = row, col
                    dx, dy = k, col
                    lx, ly = (row + k) // 2, col - (k - row) // 2
                    rx, ry = (row + k) // 2, col + (k - row) // 2

                    # Make sure left and right are within bounds
                    if ly < 0 or ry >= cols:
                        break

                    # Compute the sum and add it
                    # Add down left diag from top
                    rhombus_sum = down_left_sum[lx + 1][ly + 1] - down_left_sum[ux][uy + 2]
                    # Add down right from top diag
                    rhombus_sum += down_right_sum[rx + 1][ry + 1] - down_right_sum[ux][uy]
                    # Add down right from left diag
                    rhombus_sum += down_right_sum[dx + 1][dy + 1] - down_right_sum[lx][ly]
                    # Add down left from right diag
                    rhombus_sum += down_left_sum[dx + 1][dy + 1] - down_left_sum[rx][ry + 2]
                    # Subtract double counted squares
                    rhombus_sum -= grid[ux][uy] + grid[dx][dy] + grid[lx][ly] + grid[rx][ry]

                    top3.put(rhombus_sum)

        return top3.get()

test_cases = [
    [[228,216,211], [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]],
    [[20,9,8], [[1,2,3],[4,5,6],[7,8,9]]],
    [[7], [[7,7,7]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.getBiggestThree(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
