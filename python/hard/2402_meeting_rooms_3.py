from heapq import heappush, heappop
from typing import List


class Solution:
    # Priority queue of used rooms and unused rooms
    # Go over all meetings and see what rooms are free and put meeting there
    # Also keep array of meeting counts
    # After go through all meeting counts and pick max
    # Time O(mlogn + n + mlogm) as we go through all meetings and do log(n) push pop on it
    # Space O(n)
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms = list(range(n))
        used_rooms = []
        meeting_count = [0] * n

        # Process all meetings
        for start, end in sorted(meetings):
            # Pop all rooms that are now free
            while used_rooms and start >= used_rooms[0][0]:
                room_info = heappop(used_rooms)
                heappush(unused_rooms, room_info[1])

            # If there is an unused room use that and carry on
            if unused_rooms:
                room = heappop(unused_rooms)
                meeting_count[room] += 1
                heappush(used_rooms, (end, room))
                continue

            # If no unused rooms pop min and use it
            next_room = heappop(used_rooms)
            meeting_count[next_room[1]] += 1
            heappush(used_rooms, (next_room[0] + end - start, next_room[1]))

        # Find most used meeting room
        answer = count = 0
        for i in range(n):
            count_i = meeting_count[i]
            if count_i > count:
                count = count_i
                answer = i
 
        return answer

test_cases = [
    [0, 2, [[0,10],[1,5],[2,7],[3,4]]],
    [1, 3, [[1,20],[2,10],[3,5],[4,9],[6,8]]]
]
solution = Solution()
for expected, n, meetings in test_cases:
    actual = solution.mostBooked(n, meetings)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, meetings: {meetings}")

print("Ran all tests")