class Solution:
    # Find the furthest right 1 in each row then make swaps
    # Time O(n^2 + nlogn)
    # Space O(n)
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # Find furthest right of each row
        right_most_ones = [0] * n
        for row in range(n):
            for col in range(n-1, -1, -1):
                # Found rightmost one, set then break loop
                if grid[row][col] == 1:
                    right_most_ones[row] = col
                    break

        # Go over all rows and make sure they pass
        swaps = 0
        for i in range(n):
            swapped_row = -1
            # Go over all remaining rows and see if swap is possible
            for j in range(i, n):
                # This row is a possible swap
                if right_most_ones[j] <= i:
                    swaps += j - i
                    swapped_row = j
                    break

            # Found a row to swap
            if swapped_row != -1:
                # Do the row swapping
                for j in range(swapped_row, i, -1):
                    temp = right_most_ones[j]
                    right_most_ones[j] = right_most_ones[j-1]
                    right_most_ones[j-1] = temp
            # Found no rows to swap, so not possible
            else:
                return -1

        return swaps

test_cases = [
    [3, [[0,0,1],[1,1,0],[1,0,0]]],
    [-1, [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]],
    [0, [[1,0,0],[1,1,0],[1,1,1]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.minSwaps(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
