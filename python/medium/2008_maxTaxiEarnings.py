from collections import defaultdict
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        # Sort by start time
        rides.sort()

        # Start at end and evaluate each time if ride should be taken
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            # Check everyone who can be picked up at this i
            # decide which one would be max to pick up, or take none
            while rides and i == rides[-1][0]:
                start, end, tip = rides.pop()
                dp[i] = max(dp[i], dp[end] + end - start + tip)
                
        return dp[0]

    def maxTaxiEarningsSuboptimal(self, n: int, rides: List[List[int]]) -> int:
        rideStartAt = defaultdict(list)
        for start, end, tip in rides:
            # Each entry is in format [end, earnings]
            rideStartAt[start].append([end, end - start + tip])

        # Start at end and evaluate each time if ride should be taken
        dp = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            # A handful of these rideStartsAt entries will have nothing in them and will default to empty list
            for end, earnings in rideStartAt[i]:
                dp[i] = max(dp[i], dp[end] + earnings)
            dp[i] = max(dp[i], dp[i + 1])

        return dp[1]

testCases = [
    [5, [[2,5,4],[1,5,1]], 7],
    [20, [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]], 20]
]
solution = Solution()
for n, rides, expected in testCases:
    answer = solution.maxTaxiEarnings(n, rides)
    if answer != expected:
        print(f"FAILED TEST: Got {answer}, expected {expected}")
        print(f"INPUTS: n: {n}, rides: {rides}")