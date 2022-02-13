from bisect import bisect, bisect_left
from typing import List


class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        # Jobs sorted by increasing end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])

        # Format is [endTime, profit]
        dp = [[0, 0]]
        for start, end, profit in jobs:
            # Find previous entry where it's end time is before this start time
            i = bisect(dp, [start + 1]) - 1
            if dp[i][1] + profit > dp[-1][1]:
                dp.append([end, dp[i][1] + profit])

        return dp[-1][1]

    def jobSchedulingDP(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        startTimes = [jobs[i][0] for i in range(n)]
        memos = [0] * n

        def dp(i):
            if i == n: 
                return 0
            if memos[i] != 0:
                return memos[i]
            
            #  Don't take job i
            ans = dp(i + 1)

            # Binary search to find next available job if we take job i
            j = bisect_left(startTimes, jobs[i][1])
            # Do take job i
            ans = max(ans, dp(j) + jobs[i][2])

            memos[i] = ans
            return ans

        return dp(0)

    def jobSchedulingDP(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        memos = [0] * n

        def dp(i):
            if i == n: 
                return 0
            if memos[i] != 0:
                return memos[i]
            
            # Don't take job i 
            ans = dp(i + 1)

            # Examine all future jobs
            for j in range(i + 1, n + 1):
                # If it's the last job or if it starts after i ends
                if j == n or jobs[j][0] >= jobs[i][1]:
                    # Take job i
                    ans = max(ans, dp(j) + jobs[i][2])
                    break

            memos[i] = ans
            return ans

        return dp(0)

testCases = [
    [[1,2,3,3], [3,4,5,6], [50,10,40,70], 120],
    [[1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150],
    [[1,1,1], [2,3,4], [5,6,4], 6]
]
solution = Solution()
for starts, ends, profits, expected in testCases:
    answer = solution.jobScheduling(starts, ends, profits)
    if answer != expected:
        print(f"FAILED TEST: Got {answer}, expected {expected}")
        print(f"INPUTS: starts: {starts}, ends: {ends}, profits: {profits}")