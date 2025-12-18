from typing import List


class Solution:
    # Prefix sums to figure out where to make modifications
    # Time O(n)
    # Space O(n)
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Go over array and compute how much we've profited with strategy
        # As well as how much total prices are up til then
        profitSum = [0] * (n + 1)
        priceSum = [0] * (n + 1)
        for i in range(n):
            profitSum[i + 1] = profitSum[i] + (prices[i] * strategy[i])
            priceSum[i + 1] = priceSum[i] + prices[i]

        # Answer defaults to what strategy was if it is already optimal
        answer = profitSum[n]
        # Try to see if this window is the optimal location for the modifications
        for i in range(k - 1, n):
            # How much profit was made before modification window starts
            leftProfit = profitSum[i - k + 1]
            # How much profit was made after modification window ends
            rightProfit = profitSum[n] - profitSum[i + 1]
            # How would we profit in this window with modification
            changeProfit = priceSum[i + 1] - priceSum[i - (k // 2) + 1]
            # See if this new one is better than our current answer
            answer = max(answer, leftProfit + changeProfit + rightProfit)

        return answer

test_cases = [
    [10, [4,2,8], [-1,0,1], 2],
    [9, [5,4,3], [1,1,0], 2]
]
solution = Solution()
for expected, prices, strategy, k in test_cases:
    actual = solution.maxProfit(prices, strategy, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: prices: {prices}, strategy: {strategy}, k: {k}")

print("Ran all tests")