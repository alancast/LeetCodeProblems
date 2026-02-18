class Solution:
    # Mind numbingly simple just math comparison
    # Time O(1)
    # Space O(1)
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(x-z)
        dist2 = abs(y-z)

        if dist1 == dist2:
            return 0

        if dist1 < dist2:
            return 1

        return 2

test_cases = [
    [1, 2, 7, 4],
    [2, 2, 5, 6],
    [0, 1, 5, 3]
]
solution = Solution()
for expected, x, y, z in test_cases:
    actual = solution.findClosest(x, y, z)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: x: {x}, y: {y}, z: {z}")

print("Ran all tests")
