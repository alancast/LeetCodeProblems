from bisect import bisect_left


class Solution:
    # Sort by right endpoint and use dp to find maximum score of picking 4
    # DP stores max score indexed by index and number of intervals picked
    # Time O(nlogn + nk^2) where k is the number of intervals to pick (4 in this case)
    # Space O(nk^2)
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)

        # Transform intervals array into tuple of (right, left, weight, index)
        arr = [
            (intervals[i][1], intervals[i][0], intervals[i][2], i)
            for i in range(n)
        ]
        # Sort intervals by right endpoint
        arr.sort(key=lambda x: x[0])

        # dp[i][j] = max score of picking j intervals from first i intervals
        dp = [[0] * 5 for _ in range(n + 1)]
        indices = [[[] for _ in range(5)] for _ in range(n + 1)]

        # Go over all intervals and pick the best score of picking 4 intervals
        for i in range(n):
            _, left, weight, idx = arr[i]
            # Use binary search to find intervals whose right endpoints are smaller than l.
            k = bisect_left(arr, (left,), hi=i)

            # Update DP values based on whether we pick this interval or not
            for j in range(1, 5):
                s1 = dp[i][j]
                s2 = dp[k][j - 1] + weight
                if s1 > s2:
                    dp[i + 1][j] = dp[i][j]
                    indices[i + 1][j] = indices[i][j].copy()
                    continue

                new_index = indices[k][j - 1].copy()
                new_index.append(idx)
                new_index.sort()
                if s1 == s2 and indices[i][j] < new_index:
                    new_index = indices[i][j].copy()
                dp[i + 1][j] = s2
                indices[i + 1][j] = new_index

        # We know this is max
        return indices[n][4]

test_cases = [
    [[2,3], [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]],
    [[1,3,5,6], [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]]
]
solution = Solution()
for expected, intervals in test_cases:
    actual = solution.maximumWeight(intervals)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: intervals: {intervals}")

print("Ran all tests")
