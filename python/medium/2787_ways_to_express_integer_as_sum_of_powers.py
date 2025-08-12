class Solution:
    # DP solution space optimized going down from n to 0
    # Time O(n * xroot(n))
    # Space O(n)
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        # dp[j] = Number of ways to get j with xth powers
        dp = [0] * (n + 1)
        dp[0] = 1

        # If j<i^x, then dp[j] remains unchanged
        # If j≥i^x, then dp[j]=dp[j]+dp[j−i^x]

        # Loop over j from n to 0
        for i in range(1, n + 1):
            val = pow(i, x)
            # Can't add any combinations with this i
            if val > n:
                break

            # Add this val to all creations so far (working backwards from n)
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % MOD

        return dp[n]
    
    # DP solution
    # Time O(n^2)
    # Space O(n^2)
    def numberOfWays_space_inefficient(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] = Number of ways to get i with xth powers with none bigger than j
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # If j<i^x, then dp[i][j]=dp[i−1][j].
        # If j≥i^x, then dp[i][j]=dp[i−1][j]+dp[i−1][j−i^x]

        # Loop over i from 0 to n
        for i in range(1, n + 1):
            val = pow(i, x)
            for j in range(n + 1):
                dp[i][j] = dp[i-1][j]
                if j >= val:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD

        return dp[n][n]

test_cases = [
    [1, 10, 2],
    [2, 4, 1]
]
solution = Solution()
for expected, n, x in test_cases:
    actual = solution.numberOfWays(n, x)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, x: {x}")

print("Ran all tests")