from collections import deque
from typing import List


class Solution:
    # Go from each house to empty land and add distance to that empty land each time
    # Then update grid to be -1 for each empty land for when house can reach it
    # Only expand search into grid areas that equal the correct negative num
    # Signifying that all houses can reach them
    # If you ever reach a house that can't expand to correct negative num return -1
    # Time O(n^2*m^2)
    # Space O(n*m) as we have a full grid copy
    def shortestDistance(self, grid: List[List[int]]) -> int:
        y = len(grid)
        x = len(grid[0])
        distances = [[0 for _ in range(x)] for _ in range(y)]
        min_distance = float("inf")
        house_num = 0

        # Iterate over full grid looking for houses
        for y_idx in range(y):
            for x_idx in range(x):
                # If we have a house start bfs
                if grid[y_idx][x_idx] == 1:
                    search_target = -1 * house_num
                    house_num += 1
                    update_num = -1 * house_num
                    min_distance = float("inf")

                    q = deque()
                    # Find first neighbors if none fail
                    # Up
                    if y_idx - 1 >= 0 and grid[y_idx-1][x_idx] == search_target:
                        q.append((y_idx-1, x_idx, 1))
                    # Down
                    if y_idx + 1 < y and grid[y_idx+1][x_idx] == search_target:
                        q.append((y_idx+1, x_idx, 1))
                    # Left
                    if x_idx - 1 >= 0 and grid[y_idx][x_idx-1] == search_target:
                        q.append((y_idx, x_idx-1, 1))
                    # Right
                    if x_idx + 1 < x and grid[y_idx][x_idx+1] == search_target:
                        q.append((y_idx, x_idx+1, 1))

                    # This house couldn't get to any land
                    if not q:
                        return -1

                    # Do BFS
                    while q:
                        temp_y, temp_x, dist = q.popleft()
                        # Make sure this spot hasn't already been visited by this house
                        if grid[temp_y][temp_x] == update_num:
                            continue

                        # Append new entries to the queue and compute distances
                        # Up
                        if temp_y - 1 >= 0 and grid[temp_y-1][temp_x] == search_target:
                            q.append((temp_y-1, temp_x, dist + 1))
                        # Down
                        if temp_y + 1 < y and grid[temp_y+1][temp_x] == search_target:
                            q.append((temp_y+1, temp_x, dist + 1))
                        # Left
                        if temp_x - 1 >= 0 and grid[temp_y][temp_x-1] == search_target:
                            q.append((temp_y, temp_x-1, dist + 1))
                        # Right
                        if temp_x + 1 < x and grid[temp_y][temp_x+1] == search_target:
                            q.append((temp_y, temp_x+1, dist + 1))

                        # Update grid values and distance search
                        distances[temp_y][temp_x] += dist
                        min_distance = min(min_distance, distances[temp_y][temp_x])
                        grid[temp_y][temp_x] = update_num

        return min_distance
    
test_cases = [
    [7, [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]],
    [1, [[1,0]]],
    [-1, [[1]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.shortestDistance(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")