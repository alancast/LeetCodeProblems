from math import sqrt


class Solution:
    # Go over all dimensions and find longest diagonal
    # Store longest diagonal and largest area found with that
    # Time O(n) as we go over whole array once
    # Space O(1)
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_diagonal = largest_area = 0

        for width, height in dimensions:
            diagonal = sqrt((width*width) + (height*height))
            # See if we have a new longest diagonal
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                largest_area = width * height
            elif diagonal == max_diagonal:
                area = width * height
                largest_area = max(largest_area, area)

        return largest_area

test_cases = [
    [48, [[9,3],[8,6]]],
    [12, [[3,4],[4,3]]],
    [20, [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]]
]
solution = Solution()
for expected, dimensions in test_cases:
    actual = solution.areaOfMaxDiagonal(dimensions)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: dimensions: {dimensions}")

print("Ran all tests")
