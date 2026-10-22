import itertools


class Solution:
    # Time O(n)
    # Space O(1)
    def minOperations(self, s: str) -> int:
        n = len(s)
        mx, mn = max(s), min(s)
        if all(a <= b for a, b in itertools.pairwise(s)):
            return 0
        if n == 2:  # noqa: PLR2004
            return -1
        if s[0] == mn or s[-1] == mx:
            return 1
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
        return 3

test_cases = [
    [1, "dog"],
    [2, "card"],
    [-1, "gf"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.minOperations(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
