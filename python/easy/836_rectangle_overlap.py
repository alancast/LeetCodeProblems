class Solution:
    # Just check the edges and see if they overlap
    # Time O(1)
    # Space O(1)
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Rectangles in format [x1, y1, x2, y2]
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])

        bottom = max(rec1[1], rec2[1])
        top = min(rec1[3], rec2[3])

        return left < right and bottom < top

test_cases = [
    [True, [0,0,2,2], [1,1,3,3]],
    [False, [0,0,1,1], [1,0,2,1]],
    [False, [0,0,1,1], [2,2,3,3]]
]
solution = Solution()
for expected, rec_1, rec_2 in test_cases:
    actual = solution.isRectangleOverlap(rec_1, rec_2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: rec_1: {rec_1}, rec_2: {rec_2}")

print("Ran all tests")
