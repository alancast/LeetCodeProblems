from heapq import heappop, heappush
from typing import List


class SearchState:
    distance: int
    x: int
    y: int

    def __init__(self, distance: int, x: int, y: int):
        self.distance = distance
        self.x = x
        self.y = y

    def __lt__(self, other) -> bool:
        return self.distance < other.distance
    

class Solution:
    # Just a dykstras algorithm problem
    # Create a priority queue of time with x and y
    # Once we reach end we know it's min so return it's time
    # Once we visit a square update it's grid to -1 so it isn't added anymore
    # Time O(nm log(nm)) as we could process n*m entires, each adding a log heap push
    # Space O(1) as I did in space in the moveTime
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        final_y = len(moveTime) - 1
        final_x = len(moveTime[0]) - 1
        min_heap: List[SearchState] = []

        heappush(min_heap, SearchState(0, 0, 0))

        while min_heap:
            state = heappop(min_heap)
            # Check if reached end (if so return distance)
            if state.x == final_x and state.y == final_y:
                return state.distance
            
            # Check if already visited
            if moveTime[state.y][state.x] == -1:
                continue

            # Set moveTime to -1 to indicate visited
            moveTime[state.y][state.x] = -1

            # Check and add new entries to queue
            # Above
            if state.y - 1 >= 0 and moveTime[state.y - 1][state.x] != -1:
                next_distance = max(state.distance + 1, moveTime[state.y - 1][state.x] + 1)
                heappush(min_heap, SearchState(next_distance, state.x, state.y - 1))
            # Below
            if state.y + 1 <= final_y and moveTime[state.y + 1][state.x] != -1:
                next_distance = max(state.distance + 1, moveTime[state.y + 1][state.x] + 1)
                heappush(min_heap, SearchState(next_distance, state.x, state.y + 1))
            # Left
            if state.x - 1 >= 0 and moveTime[state.y][state.x - 1] != -1:
                next_distance = max(state.distance + 1, moveTime[state.y][state.x - 1] + 1)
                heappush(min_heap, SearchState(next_distance, state.x - 1, state.y))
            # Right
            if state.x + 1 <= final_x and moveTime[state.y][state.x + 1] != -1:
                next_distance = max(state.distance + 1, moveTime[state.y][state.x + 1] + 1)
                heappush(min_heap, SearchState(next_distance, state.x + 1, state.y))
    
test_cases = [
    [6, [[0,4],[4,4]]],
    [3, [[0,0,0],[0,0,0]]],
    [3, [[0,1],[1,2]]]
]
solution = Solution()
for expected, move_times in test_cases:
    actual = solution.minTimeToReach(move_times)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: moveTime: {move_times}")

print("Ran all tests")