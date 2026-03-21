class Solution:
    # Modify grid in place
    # Time O(k^2)
    # Space O(1)
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        # Swap rows
        top = x
        bottom = x + k - 1
        while top <= bottom:
            for col in range(y, y+k):
                temp = grid[top][col]
                grid[top][col] = grid[bottom][col]
                grid[bottom][col] = temp

            top += 1
            bottom -= 1

        return grid

test_cases = [
    [[[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]], [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3],
    [[[3,4,4,2],[2,3,2,3]], [[3,4,2,3],[2,3,4,2]], 0, 2, 2]
]
solution = Solution()
for expected, grid, x, y, k in test_cases:
    actual = solution.reverseSubmatrix(grid, x, y, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, x: {x}, y: {y}, k: {k}")

print("Ran all tests")
