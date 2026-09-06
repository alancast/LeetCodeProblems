class Solution:
    # Space optimized DP
    # Start at end of words and work back to start
    # Only care about previous row. Return dp 0
    # Time O(mn)
    # Space O(n)
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [0 for _ in range(n)]

        # Iterate over s string in reverse
        for i in range(m - 1, -1, -1):
            # At each step we start with the last value in the row which is always 1.
            prev = 1

            # Iterate over t string in reverse
            for j in range(n - 1, -1, -1):
                # Record current value in this cell to use to calculate value of dp[j - 1]
                old_dpj = dp[j]

                # If characters match, add result of next recursion call
                if s[i] == t[j]:
                    dp[j] += prev

                # Update the prev variable
                prev = old_dpj

        # Return total now that we have gotten to start
        return dp[0]

test_cases = [
    [3, "rabbbit", "rabbit"],
    [5, "babgbag", "bag"]
]
solution = Solution()
for expected, s, t in test_cases:
    actual = solution.numDistinct(s, t)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, t: {t}")

print("Ran all tests")
