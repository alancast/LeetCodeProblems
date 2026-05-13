# Definition for an Interval.
from heapq import heappop, heappush


class Interval:
    start: int | None
    end: int | None

    def __init__(self, start: int | None, end: int | None):
        self.start = start
        self.end = end

class Solution:
    # Priority queue of next up start time across all employees
    # Find range
    # Time O(nlogs) s is schedule length n is num employees
    # Space O(s) just answer space
    def employeeFreeTime(self, schedule: list[list[Interval]]) -> list[Interval]:
        # Collect first events of all employees and see start
        # Queue stores: (event.start, employee index, event index)
        pq = []
        for employee_idx, employee in enumerate(schedule):
            heappush(pq, (employee[0].start, employee_idx, 0))

        answer = []

        # Go until we have processed everything
        _, employee_idx, event_idx = pq[0]
        prev_end = schedule[employee_idx][event_idx].end
        while pq:
            event_start, employee_idx, event_idx = heappop(pq)

            # Check for next employee event and push it to pq
            if event_idx + 1 < len(schedule[employee_idx]):
                heappush(pq, (schedule[employee_idx][event_idx + 1].start, employee_idx, event_idx + 1))

            # See if we have a window where all employees are free (from checking previous end)
            if event_start > prev_end:
                answer.append(Interval(prev_end, event_start))

            # Set new end
            prev_end = max(prev_end, schedule[employee_idx][event_idx].end)

        return answer

test_cases = [
    [[[3,4]], [[[1,2],[5,6]],[[1,3]],[[4,10]]]],
    [[[5,6],[7,9]], [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]]
]
solution = Solution()
for expected, schedule in test_cases:
    # Convert list format to Interval objects
    schedule_intervals = [[Interval(start, end) for start, end in employee] for employee in schedule]
    actual = solution.employeeFreeTime(schedule_intervals)
    actual_lists = [[interval.start, interval.end] for interval in actual]
    if expected != actual_lists:
        print(f"FAILED TEST! Expected {expected} but got {actual_lists}. INPUTS: schedule: {schedule}")

print("Ran all tests")
