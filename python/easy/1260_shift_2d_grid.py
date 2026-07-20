class Solution:
    # Just make a second grid, compute next location, and fill it one by one
    # Time O(rows * cols)
    # Space O(1) just return array (could also argue n*m)
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])

        answer = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                item = grid[row][col]

                # Compute next row and col
                next_col = (col + k) % cols
                # How many rows do we need to go down
                row_movement = (col + k) // cols
                next_row = (row + row_movement) % rows

                answer[next_row][next_col] = item

        return answer

test_cases = [
    [[[9,1,2],[3,4,5],[6,7,8]], [[1,2,3],[4,5,6],[7,8,9]], 1],
    [[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]], [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4],
    [[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]], 9]
]
solution = Solution()
for expected, grid, k in test_cases:
    actual = solution.shiftGrid(grid, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, k: {k}")

print("Ran all tests")
