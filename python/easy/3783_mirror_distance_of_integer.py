class Solution:
    # Time O(1)
    # Space O(1)
    def mirrorDistance(self, n: int) -> int:
        return abs(int(str(n)[::-1]) - n)

test_cases = [
    [27, 25],
    [9, 10],
    [0, 7]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.mirrorDistance(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
