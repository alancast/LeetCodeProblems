class Solution:
    # Just do the math and check overlap
    # Time O(1)
    # Space O(1)
    def checkOverlap(  # noqa: PLR0913, PLR0917
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # Find minimum distance from circle center to rectangle
        dist = 0
        if xCenter < x1 or xCenter > x2:
            dist += min((x1 - xCenter) ** 2, (x2 - xCenter) ** 2)
        if yCenter < y1 or yCenter > y2:
            dist += min((y1 - yCenter) ** 2, (y2 - yCenter) ** 2)

        # Return true if distance is less than or equal to radius squared (to avoid sqrt)
        return dist <= radius**2

test_cases = [
    [True, 1, 0, 0, 1, -1, 3, 1],
    [False, 1, 1, 1, 1, -3, 2, -1],
    [True, 1, 0, 0, -1, 0, 0, 1],
]
solution = Solution()
for expected, radius, xCenter, yCenter, x1, y1, x2, y2 in test_cases:
    actual = solution.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")

print("Ran all tests")
