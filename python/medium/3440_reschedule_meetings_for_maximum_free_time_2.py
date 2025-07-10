from typing import List


class Solution:
    # Go over all meetings. Keep track of largest open space to left (and right)
    # of this meeting and see if meeting can fully slot into open space or just slide
    # next to adjacent meetings. Update max each time
    # Time O(n) as we go through array once and do O(1) ops
    # Space O(1)
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # Assuming startTime and endTime are sorted, if not just sort them
        n = len(startTime)
        answer = free_space = free_space_2 = 0

        for i in range(n):
            # Find left time bound
            left = 0
            if i > 0:
                left = endTime[i-1]

            # Find right time bound
            right = eventTime
            if i < n-1:
                right = startTime[i+1]

            # See if this entire meeting can be slotted into an earlier free space
            duration = endTime[i] - startTime[i]
            if duration <= free_space:
                answer = max(answer, right - left)

            # Update biggest free space
            free_space = max(free_space, startTime[i] - left)

            # Update answer if this meeting is too long to fit into another time slot
            answer = max(answer, right - left - duration)

            # Also go from right to left
            left_2 = 0
            if i < n - 1:
                left_2 = endTime[n-i-2]
            
            right_2 = eventTime
            if i > 0:
                right_2 = startTime[n-i]

            # See if meeting at end can slot into different time slot
            duration_2 = endTime[n-i-1] - startTime[n-i-1]
            if duration_2 <= free_space_2:
                answer = max(answer, right_2 - left_2)

            # Update free_space_2
            free_space_2 = max(free_space_2, right_2 - endTime[n-i-1])

        return answer
    
test_cases = [
    [2, 5, [1,3], [2,5]],
    [7, 10, [0,7,9], [1,8,10]],
    [6, 10, [0,3,7,9], [1,4,8,10]],
    [0, 5, [0,1,2,3,4], [1,2,3,4,5]]
]
solution = Solution()
for expected, event_time, start_time, end_time in test_cases:
    actual = solution.maxFreeTime(event_time, start_time, end_time)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: event_time: {event_time}, start_time: {start_time}, end_time: {end_time}")

print("Ran all tests")