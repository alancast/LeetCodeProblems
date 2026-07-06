class Solution:
    # Greedy sort by start time and latest end time
    # Time O(nlogn) for sort
    # Space O(n)
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        n = len(intervals)

        # Sort by start time and then latest end time
        intervals = sorted(intervals, key= lambda x: (x[0], -x[1]))
        count_covered = 0
        previousEnd = -1

        # Go over all intervals and see how many end before previous
        # We know start will always increase
        for interval in intervals:
            end = interval[1]
            if end <= previousEnd:
                count_covered += 1
            else:
                previousEnd = end

        # Just subtract how many are covered from total
        return n - count_covered

testCases = [
    [[[1,4],[3,6],[2,8]], 2],
    [[[1,4],[2,3]], 1]
]
implementation = Solution()
for intervals, expected in testCases:
    answer = implementation.removeCoveredIntervals(intervals)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. INPUT: {intervals}")

print("Ran all tests")
