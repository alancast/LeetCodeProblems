from typing import List


class Solution:
    # Time O(nlogn) as we call sort which is nlogn 
    # Space O(S) where whatever the sort solution takes up
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        # Try both horizontal (0) and vertical (1) cuts
        return self._check_cuts(rectangles, 0) or self._check_cuts(rectangles, 1)

    # Check if valid cuts can be made in a specific dimension (0=x 1=y)
    def _check_cuts(self, rectangles: list[list[int]], dim: int) -> bool:
        gap_count = 0

        # Sort rectangles by their starting coordinate in the given dimension
        rectangles.sort(key=lambda rect: rect[dim])

        # Track the furthest ending coordinate seen so far
        furthest_end = rectangles[0][dim + 2]

        # Go through all rectangles and see if gaps exist
        for i in range(1, len(rectangles)):
            rect = rectangles[i]

            # If rectangle starts after the furthest end we found a gap
            if furthest_end <= rect[dim]:
                gap_count += 1
                if gap_count == 2:
                    return True

            # Update the furthest ending coordinate
            furthest_end = max(furthest_end, rect[dim + 2])

        # We didn't find 2 gaps
        return False

test_cases = [
    [True, 5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]],
    [True, 4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]],
    [False, 4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]]
]
solution = Solution()
for expected, n, rectangles in test_cases:
    actual = solution.checkValidCuts(n, rectangles)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, rectangles: {rectangles}")

print("Ran all tests")