class Solution:
    # DP solution where we compute probability that a number occurs
    # Time O(n)
    # Space O(n)
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Initialize DP array and set dp[0] to 1 cuz guaranteed to start there
        dp = [0] * (n + 1)
        dp[0] = 1

        # DP sum of all probs of nums smaller than k
        probs_sum_smaller_k = 1
        if k == 0:
            probs_sum_smaller_k = 0

        for i in range(1, n + 1):
            # Update DP entry to sum * 1/max_points prob
            dp[i] = probs_sum_smaller_k / maxPts

            # If i less than k add to probs sum
            if i < k:
                probs_sum_smaller_k += dp[i]
            
            # Roll off back end of sliding window max points in the past
            if i - maxPts >= 0 and i - maxPts < k:
                probs_sum_smaller_k -= dp[i - maxPts]

        # Sum up all values k to n
        return sum(dp[k:])
    
test_cases = [
    [1.00000, 10, 1, 10],
    [.60000, 6, 1, 10],
    [.73278, 21, 17, 10]
]
solution = Solution()
for expected, n, k, max_pts in test_cases:
    actual = solution.new21Game(n, k, max_pts)
    if round(expected, 5) != round(actual, 5):
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, k: {k}, maxPts: {max_pts}")

print("Ran all tests")