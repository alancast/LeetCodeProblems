from collections import defaultdict, deque
from typing import List

# Time O(R*C) as we go over the full grid a couple times
# Space O(R*C) as we store a set of all R C combos
def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    # Create portal map as well as find starting location
    start_row = start_col = 0
    portal_map = defaultdict(list)
    for row in range(R):
        for col in range(C):
            cell = G[row][col]
            # Don't do anything with wall exit or empty cells
            if cell in '.E#':
                continue

            if cell == 'S':
                start_row = row
                start_col = col
                continue

            portal_map[cell].append((row, col))

    # Do BFS search to find exit
    queued = set()
    queue = deque()
    queue.append((start_row, start_col, 0))
    queued.add((start_row, start_col))
    while queue:
        cur_row, cur_col, cur_time = queue.popleft()

        cur_cell = G[cur_row][cur_col]
        # We've found an exit
        if cur_cell == 'E':
            return cur_time

        # If it's a portal append to queue all it's others
        if cur_cell in portal_map:
            for neighbor_row, neighbor_col in portal_map[cur_cell]:
                # Don't append our own cell
                if (neighbor_row, neighbor_col) in queued:
                    continue

                queue.append((neighbor_row, neighbor_col, cur_time + 1))
                queued.add((neighbor_row, neighbor_col))

            # delete it's entries as they are now redundant
            portal_map[cur_cell].clear()

        # Append all valid neighbors
        # Check left
        if (
            cur_col - 1 >= 0
            and (cur_row, cur_col - 1) not in queued
            and G[cur_row][cur_col - 1] != '#'
        ):
            queue.append((cur_row, cur_col - 1, cur_time + 1))
            queued.add((cur_row, cur_col - 1))
        # Check right
        if (
            cur_col + 1 < C
            and (cur_row, cur_col + 1) not in queued
            and G[cur_row][cur_col + 1] != '#'
        ):
            queue.append((cur_row, cur_col + 1, cur_time + 1))
            queued.add((cur_row, cur_col + 1))
        # Check up
        if (
            cur_row - 1 >= 0
            and (cur_row - 1, cur_col) not in queued
            and G[cur_row - 1][cur_col] != '#'
        ):
            queue.append((cur_row - 1, cur_col, cur_time + 1))
            queued.add((cur_row - 1, cur_col))
        # Check down
        if (
            cur_row + 1 < R
            and (cur_row + 1, cur_col) not in queued
            and G[cur_row + 1][cur_col] != '#'
        ):
            queue.append((cur_row + 1, cur_col, cur_time + 1))
            queued.add((cur_row + 1, cur_col))
            
    return -1

test_cases = [
    [4, 3, 3, [['.','E','.'],['.','#','E'],['.','S','#']]],
    [-1, 3, 4, [['a','.','S','a'],['#','#','#','#'],['E','b','.','b']]],
    [4, 3, 4, [['a','S','.','b'],['#','#','#','#'],['E','b','.','a']]],
    [3, 1, 9, [['x','S','.','.','x','.','.','E','x']]]
]
for expected, R, C, G in test_cases:
    actual = getSecondsRequired(R, C, G)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: R: {R}, C: {C}, G: {G}")

print("Ran all tests")