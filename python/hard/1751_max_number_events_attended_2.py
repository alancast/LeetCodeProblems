from bisect import bisect_right
from typing import List


class Solution:
    # DP solution
    # Time O(nklogn) as sorting is nlogn 2d array of nk that does logn binary search
    # Space O(nk) for dp array
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)

        start_times = [start for start, _, _ in events]
        dp = [[-1] * n for _ in range(k + 1)]
        
        def dfs(cur_index, k):
            # No events left to take or at end of list
            if k == 0 or cur_index == n:
                return 0
            
            # Subproblem already computed
            if dp[k][cur_index] != -1:
                return dp[k][cur_index]

            # Find the nearest available event after attending event 0
            next_index = bisect_right(start_times, events[cur_index][1])

            # See if better to go or not 
            go = events[cur_index][2] + dfs(next_index, k - 1)
            dont = dfs(cur_index + 1, k)
            dp[k][cur_index] = max(dont, go)

            return dp[k][cur_index]
        
        return dfs(0, k)
    
    # Recursive solution. Sort by start time and at every event
    # Find score if you go or not
    # Time O(2^n) as for every event we evaluate going and not going
    # Space O(n) for recursive call stack
    def maxValue_recursive(self, events: List[List[int]], k: int) -> int:
        self.n = len(events)
        events.sort()

        return self._max_value_helper(events, k, 0, 0)
    
    def _max_value_helper(
            self, 
            events: List[List[int]], 
            k: int, 
            index: int, 
            free_time: int
        ) -> int:

        if index == self.n or k == 0:
            return 0

        start, end, value = events[index]

        # Can't go to the event
        if start <= free_time:
            return self._max_value_helper(events, k, index + 1, free_time)
        
        # Can go to event so try going to it and not
        go = value + self._max_value_helper(events, k - 1, index + 1, end)

        # Don't go
        dont = self._max_value_helper(events, k, index + 1, free_time)
        
        return max(go, dont)
    
test_cases = [
    [7, [[1,2,4],[3,4,3],[2,3,1]], 2],
    [10, [[1,2,4],[3,4,3],[2,3,10]], 2],
    [9, [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3]
]
solution = Solution()
for expected, events, k in test_cases:
    actual = solution.maxValue(events, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: events: {events}, k: {k}")

print("Ran all tests")