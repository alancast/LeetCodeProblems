class Solution:
    # DP math formula
    # Whether to copy paste or add an A, sometimes paste multiple in a row
    # Time O(n)
    # Space O(n)
    def maxA(self, n: int) -> int:
        dp = list(range(n + 1))

        for i in range(n - 2):
            for j in range(i + 3, min(n, i + 6) + 1):
                dp[j] = max(dp[j], (j - i - 1) * dp[i])

        return dp[n]

test_cases = [
    [3, 3],
    [9, 7]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.maxA(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
