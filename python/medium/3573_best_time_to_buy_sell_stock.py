from typing import List


class Solution:
    # Dynamic programming
    # Keep track of how much you could have if the previous day you:
    # Had a stock, didn't have a stock, had x transactions left, and do y today
    # dp[i][j][k] i signifies what day, j signifies how many completed transactions, 
    # k signifies if empty (0) holding (1) shorting (2)
    # Time O(nk) go over all n days and all k transaction left options
    # Space O(k)
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # 
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]

        # On day 0 you can buy ([0][j][1]) or sell ([0][j][2]) or nothing ([0][j][0])
        # You are doing at least 1 transaction here so must update j 1 through k
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]
            dp[0][j][2] = prices[0]

        # Go over all the days and evaluate each action (buy, sell, hold)
        for i in range(1, n):
            # Update all numbers of completed transactions (1 through k)
            for j in range(1, k + 1):
                # If you are not holding it's max of:
                dp[i][j][0] = max(
                    # Yesterday not holding, 
                    dp[i - 1][j][0],
                    # Yesterday holding and sell today, 
                    dp[i - 1][j][1] + prices[i],
                    # Yesterday short and buy today
                    dp[i - 1][j][2] - prices[i]
                )
                # If you are holding it's max of:
                dp[i][j][1] = max(
                    # Yesterday holding and nothing today
                    dp[i - 1][j][1],
                    # Yesterday nothing and buy today
                    dp[i - 1][j - 1][0] - prices[i]
                )
                # If you are shorting it's max of:
                dp[i][j][2] = max(
                    # Yesterday short and nothing today
                    dp[i - 1][j][2],
                    # Yesterday nothing and short today
                    dp[i - 1][j - 1][0] + prices[i]
                )

        # Answer is final day, all k trades, not holding anything
        return dp[n - 1][k][0]

test_cases = [
    [9, [1,7,9,10], 2],
    [14, [1,7,9,8,2], 2],
    [36, [12,16,19,19,8,1,19,13,9], 3]
]
solution = Solution()
for expected, prices, k in test_cases:
    actual = solution.maximumProfit(prices, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: prices: {prices}, k: {k}")

print("Ran all tests")