from heapq import heappop, heappush
from typing import List


class Solution:
    # Min heap
    # Time O(nlogn)
    # Space O(n)
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Create a list to store the pair (end time, value) for events
        pq = []

        # Sort the events by their start time
        events.sort(key=lambda x: x[0])

        max_val = 0
        answer = 0

        # Go over all events and any time we have one that starts after one ended
        # Take that event and see if it can be a new max
        for event in events:
            # If the queue has events that end before this starts
            # pop them all and take the max value of them
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heappop(pq)

            # Compute max sum by adding this event to the already ended max
            answer = max(answer, max_val + event[2])

            # Push the current event's end time and value into the heap
            heappush(pq, (event[1], event[2]))

        return answer

    # Double list entries by creating one for start and one for end
    # Then sort based on time, and go over once and compute answer
    # Time O(nlogn) for sort
    # Space O(n) (really 2 n)
    def maxTwoEvents_single_pass(self, events: List[List[int]]) -> int:
        times = []
        for event in events:
            # 1 denotes start time.
            times.append([event[0], 1, event[2]])
            # 0 denotes end time.
            times.append([event[1] + 1, 0, event[2]])

        answer = max_value = 0
        # Sorts times. If two times have same value, end time goes first
        times.sort()

        # Know that we will only take at most 2 events because we only ever set
        # max_value when it's an end event. So answer is always at most
        # a combination of start value with 1 other event
        for _, type, value in times:
            # If a start time, find maximum sum of maximum end time till now.
            if type:
                answer = max(answer, value + max_value)
            # If it's an end time see if it's best to just take this event
            else:
                max_value = max(max_value, value)

        return answer

    # Sort by start time and DP
    # DP of max at given time and how many events used so far
    # Time O(nlogn)
    # Space O(n)
    def maxTwoEvents_dp(self, events: List[List[int]]) -> int:
        # Sort by start time
        events.sort()
        # DP array of max possible to get there with 0, 1, or 2 events used
        dp = [[-1] * 3 for _ in range(len(events))]
        return self.find_events(events, 0, 0, dp)

    # Recursive function to find the greatest sum for the pairs.
    def find_events(
            self, 
            events: List[List[int]], 
            idx: int, 
            cnt: int, 
            dp: List[List[int]]
    ) -> int:
        # We have already picked 2 events or are at end
        if cnt == 2 or idx >= len(events):
            return 0

        # This entry has not been compute, so do that
        if dp[idx][cnt] == -1:
            end = events[idx][1]

            # Do binary search to find index we need to jump to if we take this event
            low = idx + 1
            high = len(events) - 1
            while low < high:
                # To avoid overflow
                mid = low + ((high - low) // 2)
                if events[mid][0] > end:
                    high = mid
                else:
                    low = mid + 1
            
            # Compute score if we include this event
            include = events[idx][2]
            # See if we can also add an event after this one
            if low < len(events) and events[low][0] > end:
                include = events[idx][2] + self.find_events(events, low, cnt + 1, dp)

            # Compute score if we don't include the event
            exclude = self.find_events(events, idx + 1, cnt, dp)

            # Compute max of including or not
            dp[idx][cnt] = max(include, exclude)

        # After processing all options return max
        return dp[idx][cnt]

    # Sort by event weight, then evaluate pairs
    # Time O(nlogn + n^2)
    # Space O(n)
    def maxTwoEvents_brute_force(self, events: List[List[int]]) -> int:
        n = len(events)

        # Sort by event value
        events.sort(key=lambda e: e[2], reverse=True)

        answer = events[0][2]
        # Go over all event pairs and try to find max
        for i in range(n):
            start_one, end_one, value_one = events[i]
            # See if no possible combination with this is better
            if value_one <= answer // 2:
                break

            # Find second event to pair with
            for j in range(i+1, n):
                start_two, end_two, value_two = events[j]

                # See if this pair is even worth evaluating
                if value_one + value_two <= answer:
                    break

                # See if possible pairing and if so break
                if start_two > end_one or end_two < start_one:
                    answer = value_one + value_two
                    break

        return answer

test_cases = [
    [4, [[1,3,2],[4,5,2],[2,4,3]]],
    [5, [[1,3,2],[4,5,2],[1,5,5]]],
    [8, [[1,5,3],[1,5,1],[6,6,5]]]
]
solution = Solution()
for expected, events in test_cases:
    actual = solution.maxTwoEvents(events)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: events: {events}")

print("Ran all tests")
