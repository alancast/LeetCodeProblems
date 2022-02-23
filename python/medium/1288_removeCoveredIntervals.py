from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals = sorted(intervals, key= lambda x: (x[0], -x[1]))
        count = 0
        previousEnd = -1

        for interval in intervals:
            end = interval[1]
            if end <= previousEnd:
                count += 1
            else:
                previousEnd = end

        return len(intervals) - count

testCases = [
    [[[1,4],[3,6],[2,8]], 2],
    [[[1,4],[2,3]], 1]
]
implementation = Solution()
for intervals, expected in testCases:
    answer = implementation.removeCoveredIntervals(intervals)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. INPUT: {intervals}")