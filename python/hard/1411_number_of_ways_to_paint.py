class Solution:
    MOD = 10**9 + 7

    # Math
    # Time O(n)
    # Space O(1)
    def numOfWays(self, n: int) -> int:
        # Base counts for n == 1:
        # A = number of "same" color patterns for the first column (6)
        # B = number of "different" color patterns for the first column (6)
        A = B = 6

        # Build up from column 1 to column n using the recurrence:
        # newA = 2*A + 2*B   (ways to form a "same" pattern from previous A or B)
        # newB = 2*A + 3*B   (ways to form a "diff" pattern from previous A or B)
        # Iterate from 2 to n (inclusive) to apply the transition n-1 times.
        for _ in range(2, n + 1):
            A, B = (2*A + 2*B) % self.MOD, (2*A + 3*B) % self.MOD

        # Total ways for n columns is sum of both pattern types (modded)
        return (A + B) % self.MOD

test_cases = [
    [12, 1],
    [30228214, 5000]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.numOfWays(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")