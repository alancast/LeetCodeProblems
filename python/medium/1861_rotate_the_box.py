class Solution:
    # Just do the rotation. Keep track of last obstacle on rotation and fill accordingly
    # Time O(mn)
    # Space O(1) just return space
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        m = len(box)
        n = len(box[0])
        # Initially make everything empty
        result = [["." for _ in range(m)] for _ in range(n)]

        # Apply gravity to let stones fall to the lowest possible empty cell in each column
        for i in range(m):
            lowest_row_with_empty_cell = n - 1
            # Process each cell in row `i` in reversed order
            for j in range(n - 1, -1, -1):
                # Found a stone - let it fall to the lowest empty cell
                if box[i][j] == "#":
                    # Place it in the correct position in the rotated grid
                    result[lowest_row_with_empty_cell][m - i - 1] = "#"
                    lowest_row_with_empty_cell -= 1
                # Found an obstacle - reset `lowest_row_with_empty_cell` to the row directly above it
                if box[i][j] == "*":
                    # Place the obstacle in the correct position in the rotated grid
                    result[j][m - i - 1] = "*"
                    lowest_row_with_empty_cell = j - 1

        return result
