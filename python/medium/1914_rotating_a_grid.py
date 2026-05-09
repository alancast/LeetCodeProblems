class Solution:
    # Very poorly worded question. Also leetcode is really on a rotation kick right now
    # But basically just do all the rotations
    # Time O(mn)
    # Space O(m + n)
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])

        # Level count (very poorly worded question)
        num_layers = min(m // 2, n // 2)

        # enumerate each layer counterclockwise starting from the top-left corner
        for layer in range(num_layers):
            r = []  # row index of each element
            c = []  # column index of each element
            val = []  # value of each element
            for i in range(layer, m - layer - 1):  # left
                r.append(i)
                c.append(layer)
                val.append(grid[i][layer])
            for j in range(layer, n - layer - 1):  # down
                r.append(m - layer - 1)
                c.append(j)
                val.append(grid[m - layer - 1][j])
            for i in range(m - layer - 1, layer, -1):  # right
                r.append(i)
                c.append(n - layer - 1)
                val.append(grid[i][n - layer - 1])
            for j in range(n - layer - 1, layer, -1):  # up
                r.append(layer)
                c.append(j)
                val.append(grid[layer][j])

            total = len(val)  # total number of elements in each layer
            kk = k % total  # equivalent number of rotations

            # find the value at each index after rotation
            for i in range(total):
                idx = (
                    i + total - kk
                ) % total  # the index corresponding to the value after rotation
                grid[r[i]][c[i]] = val[idx]

        return grid

test_cases = [
    [[[10,20],[40,30]], [[40,10],[30,20]], 1],
    [[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]], [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2]
]
solution = Solution()
for expected, grid, k in test_cases:
    actual = solution.rotateGrid(grid, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, k: {k}")

print("Ran all tests")
