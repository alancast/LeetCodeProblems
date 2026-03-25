class Solution:
    # Go over grid once to find sum, and store horizontal cut sums
    # Then try once with vertical cuts
    # Time O(mn)
    # Space O(n) for horizontal sum storage (possible in O(1) but slower)
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        # Go over once and find total sum and store horizontal cut nums
        horizontal_sums = set()
        sum = 0
        for row in grid:
            for entry in row:
                sum += entry

            horizontal_sums.add(sum)

        # Impossible if sum is odd
        if sum %2 == 1:
            return False

        # See if half was found in horizontal
        target = sum // 2
        if sum // 2 in horizontal_sums:
            return True

        # Now go over grid via vertical cuts and see if it is possible
        sum = 0
        for col in range(cols):
            for row in range(rows):
                sum += grid[row][col]

            if sum == target:
                return True

        # Wasn't possible via vertical cuts either
        return False

test_cases = [
    [True, [[1,4],[2,3]]],
    [False, [[1,3],[2,4]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.canPartitionGrid(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
