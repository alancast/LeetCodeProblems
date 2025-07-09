from typing import List


class Solution:
    # Sliding window of meeting times and duration span
    # Find window length of k+1 meetings minus duration, return max of that
    # Time O(n) as go through list once
    # Space O(1)
    def maxFreeTime(
        self,
        eventTime: int,
        k: int,
        startTime: List[int],
        endTime: List[int]
    ) -> int:
        # Assuming startTime and endTime are sorted, if not just sort them
        n = len(startTime)
        answer = duration_busy = 0

        for i in range(n):
            duration_busy += endTime[i] - startTime[i]

            # Start time is either 0 or whenever the meeting before ended
            start_time = 0
            if i >= k:
                start_time = endTime[i-k]

            # End time is either event time or start of next meeting
            end_time = eventTime
            if i < n - 1:
                end_time = startTime[i+1]

            # Figure out if answer is new max
            span = end_time - start_time
            answer = max(answer, span - duration_busy)

            # Remove meeting that slid out of range of window
            if i >= k - 1:
                duration_busy -= endTime[i - k + 1] - startTime[i - k + 1]

        return answer
    
test_cases = [
    [2, 5, 1, [1,3], [2,5]],
    [18, 34, 2, [0,17], [14,19]],
    [2, 30, 2, [1,15,17], [14,17,29]],
    [6, 10, 1, [0,2,9], [1,4,10]],
    [0, 5, 2, [0,1,2,3,4], [1,2,3,4,5]]
]
solution = Solution()
for expected, event_time, k, start_time, end_time in test_cases:
    actual = solution.maxFreeTime(event_time, k, start_time, end_time)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: event_time: {event_time}, k: {k}, start_time: {start_time}, end_time: {end_time}")

print("Ran all tests")