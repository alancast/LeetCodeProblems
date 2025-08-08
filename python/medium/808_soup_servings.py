from collections import defaultdict
from functools import cache
from math import ceil


class Solution:
    # Really optimized for speed but same idea as below
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        
        n = (n+24) // 25

        @cache
        def dp(a,b):
            if a <= 0 and b<= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            
            return 0.25 * (dp(a-4, b) + dp(a-3,b-1) + dp(a-2, b-2) + dp(a-1, b-3))
        
        return dp(n, n)

    # DP to compute probability of final answer
    # Time O(servings^2)
    # Space O(servings^2)
    def soupServings_readable(self, n: int) -> float:
        servings = ceil(n/25)

        # Dictionary with servings of A and servings of B left
        dp = defaultdict(dict)

        def calculate_dp(i: int, j: int) -> float:
            # Base cases
            # Half of prob they both run out at same time (so 1 / 2)
            if i <= 0 and j <= 0:
                return 0.5
            # A ran out first
            if i <= 0:
                return 1.0
            # B ran out first
            if j <= 0:
                return 0.0
            
            # If it's already been calculated just return that value
            if i in dp and j in dp[i]:
                return dp[i][j]

            # Compute the probability for this value
            dp[i][j] = (
                calculate_dp(i - 4, j)
                + calculate_dp(i - 3, j - 1)
                + calculate_dp(i - 2, j - 2)
                + calculate_dp(i - 1, j - 3)
            ) / 4.0

            # Return the answer
            return dp[i][j]

        # Compute from 1 up to servings. 
        # If it ever gets close enough to 1 just cut it off and return 1
        for k in range(1, servings + 1):
            if calculate_dp(k, k) > 1 - 1e-5:
                return 1.0
            
        return calculate_dp(servings, servings)
    
test_cases = [
    [.62500, 50],
    [.71875, 100]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.soupServings(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")