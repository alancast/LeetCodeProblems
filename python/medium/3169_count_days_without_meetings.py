from typing import List


class Solution:
    # Time O(nlogn) as we sort the meetings and then just go through it
    # Space O(S) where s is however much space the sorting algo takes up
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        answer = 0
        # it's 1 indexed in days
        last_meeting_day = 1
        meetings.sort(key=lambda x: x[0])

        for start, end in meetings:
            if start > last_meeting_day:
                answer += start - last_meeting_day

            # +1 because end is inclusive
            last_meeting_day = max(last_meeting_day, end + 1)

        if days >= last_meeting_day:
            answer += days - last_meeting_day + 1

        return answer
    
test_cases = [
    [0, 10, [[1,10]]],
    [1, 2, [[1,1]]],
    [9, 10, [[1,1]]],
    [0, 1, [[1,1]]],
    [2, 10, [[5,7], [1,3], [9,10]]]
]
solution = Solution()
for expected, days, meetings in test_cases:
    actual = solution.countDays(days, meetings)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: days: {days}, meetings: {meetings}")

print("Ran all tests")