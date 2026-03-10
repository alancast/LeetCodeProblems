class Solution:
    MOD = 10**9 + 7

    # Deceptively tricky combinatorics problem
    # Time O(zero * one)
    # Space O(zero * one)
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # dp[i][j] Number of ways to have [i] zeros and and [j] ones
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        # Fill in all initial pure zero combinations
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        # Fill in all initial pure one combinations
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1

        # Fill out remainder of dp
        for zeros in range(1, zero + 1):
            for ones in range(1, one + 1):
                # Handle zeros
                if zeros > limit:
                    dp[zeros][ones][0] = (
                        dp[zeros - 1][ones][0]
                        + dp[zeros - 1][ones][1]
                        - dp[zeros - limit - 1][ones][1]
                    )
                else:
                    dp[zeros][ones][0] = dp[zeros - 1][ones][0] + dp[zeros - 1][ones][1]

                dp[zeros][ones][0] = dp[zeros][ones][0] % self.MOD

                # Handle ones
                if ones > limit:
                    dp[zeros][ones][1] = (
                        dp[zeros][ones - 1][1]
                        + dp[zeros][ones - 1][0]
                        - dp[zeros][ones - limit - 1][0]
                    )
                else:
                    dp[zeros][ones][1] = dp[zeros][ones - 1][1] + dp[zeros][ones - 1][0]

                dp[zeros][ones][1] = dp[zeros][ones][1] % self.MOD

        # Return combination of ending with zero and ending with one
        return (dp[zero][one][0] + dp[zero][one][1]) % self.MOD

test_cases = [
    [2, 1, 1, 2],
    [1, 1, 2, 1],
    [14, 3, 3, 2]
]
solution = Solution()
for expected, zero, one, limit in test_cases:
    actual = solution.numberOfStableArrays(zero, one, limit)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: zero: {zero}, one: {one}, limit {limit}")

print("Ran all tests")
