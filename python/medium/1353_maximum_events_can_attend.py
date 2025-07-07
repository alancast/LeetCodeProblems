from heapq import heappush, heappop
from typing import List


class Solution:
    # Sort and greedy
    # Time O((T+n)logn) as we sort the list then go over all T days with logn operations
    # Space O(n) for sorting algorithm as well as min heap
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()

        min_heap = []
        answer = event_index = 0
        # Go over all days
        for i in range(1, max_day + 1):
            # Push all events that we could go to (start before this day) to min_heap
            while event_index < n and events[event_index][0] <= i:
                # Only push end date to min_heap
                heappush(min_heap, events[event_index][1])
                event_index += 1
            # Purge all older events that we can't go to as they ended before today
            while min_heap and min_heap[0] < i:
                heappop(min_heap)
            # If there is anything in the heap go to it today and pop it
            if min_heap:
                heappop(min_heap)
                answer += 1

        return answer
    
test_cases = [
    [3, [[1,2], [2,3], [3,4]]],
    [4, [[1,2], [2,3], [3,4], [1,2]]],
    [4, [[1,4],[4,4],[2,2],[3,4],[1,1]]]
]
solution = Solution()
for expected, events in test_cases:
    actual = solution.maxEvents(events)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: events: {events}")

print("Ran all tests")