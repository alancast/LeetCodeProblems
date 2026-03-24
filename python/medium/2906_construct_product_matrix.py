class Solution:
    MOD = 12345

    # Find product by going over twice, once for prefix once for suffix
    # Time O(mn)
    # Space O(1)
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])

        answer = [[0] * cols for _ in range(rows)]

        # Compute product for all items in matrix after this item (suffix)
        suffix = 1
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                answer[row][col] = suffix
                suffix = (suffix * grid[row][col]) % self.MOD

        # Compute product for all items in matrix before this item (prefix)
        prefix = 1
        for row in range(rows):
            for col in range(cols):
                answer[row][col] = (answer[row][col] * prefix) % self.MOD
                prefix = (prefix * grid[row][col]) % self.MOD

        return answer

    # This takes too long as multiplication gets too big
    # Find product of full matrix then just divide at each grid
    # Time O(mn)
    # Space O(1)
    def constructProductMatrix_too_slow(self, grid: list[list[int]]) -> list[list[int]]:
        product = 1

        # Find total product
        for row in grid:
            for entry in row:
                product *= entry

        # Construct answer
        answer = []
        for row in grid:
            product_row = []
            for entry in row:
                product_row.append((product//entry)%self.MOD)

            answer.append(product_row)

        return answer

test_cases = [
    [[[24,12],[8,6]], [[1,2],[3,4]]],
    [[[2],[0],[0]], [[12345],[2],[1]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.constructProductMatrix(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
