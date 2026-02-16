from bisect import bisect_right


class Solution:
    # Can take advantage of fact that both rows and columns are sorted
    # Do in linear time
    # Time O(m+n)
    # Space O(1)
    def countNegatives(self, grid: list[list[int]]) -> int:
        # Length of each row
        n = len(grid[0])

        answer = 0
        # At first row start at farthest right and see where we find negative
        negative_index = n - 1

        # Iterate on all rows of the matrix one by one.
        for row in grid:
            # Find first positive number in row
            while negative_index >= 0 and row[negative_index] < 0:
                negative_index -= 1

            # Add all negative numbers to answer and then do next row
            answer += (n - (negative_index + 1))

        return answer

    # Binary search to find negative index in each row
    # Time O(mlogn)
    # Space O(1)
    def countNegatives_binary_search(self, grid: list[list[int]]) -> int:
        # Length of each row
        n = len(grid[0])

        answer = 0
        # Iterate on all rows of the matrix one by one.
        for row in grid:
            # Binary search to find the first negative element.
            left = bisect_right([-x for x in row], 0)

            # 'left' points to the first negative element,
            # which means 'n - left' is the number of all negative elements.
            answer += (n - left)

        return answer

test_cases = [
    [8, [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]],
    [0, [[3,2],[1,0]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.countNegatives(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
