class Solution:
    # Time O(logn)
    # Space O(logn)
    def rotatedDigits(self, n: int) -> int:
        dp = [0] * (n + 1)
        count = 0

        for i in range(n + 1):
            if i < 10:  # noqa: PLR2004
                if i in (0, 1, 8):
                    dp[i] = 1
                elif i in (2, 5, 6, 9):
                    dp[i] = 2
                    count += 1
                else:
                    dp[i] = 0
            else:
                a = dp[i // 10]
                b = dp[i % 10]

                if a == 1 and b == 1:
                    dp[i] = 1
                elif a >= 1 and b >= 1:
                    dp[i] = 2
                    count += 1
                else:
                    dp[i] = 0

        return count

test_cases = [
    [4, 10],
    [0, 1],
    [1,2]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.rotatedDigits(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
