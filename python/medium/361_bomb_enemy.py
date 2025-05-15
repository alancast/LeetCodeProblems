from typing import List


class Solution:
    # Two pass solution go through all m x n twice and find max
    # Time O(m*n)
    # Space O(m*n) as we have something of size grid
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        y = len(grid)
        x = len(grid[0])

        # Create row_count and col_count grids
        row_count = [[0 for _ in range(x)] for _ in range(y)]
        col_count = [[0 for _ in range(x)] for _ in range(y)]

        # Process each col
        for i in range(x):
            count = 0
            start = 0
            end = 0
            while end < y:
                # We hit a wall, count stops, propagate start to end with count
                if grid[end][i] == 'W':
                    for j in range(start, end):
                        col_count[j][i] = count

                    count = 0
                    start = end + 1
                elif grid[end][i] == 'E':
                    count += 1

                end += 1

            # Process til end of row
            for j in range(start, end):
                col_count[j][i] = count
        
        # Process each row and while doing so find max
        answer = 0
        for i in range(y):
            count = 0
            start = 0
            end = 0
            while end < x:
                # We hit a wall, count stops, propagate start to end with count
                if grid[i][end] == 'W':
                    for j in range(start, end):
                        row_count[i][j] = count

                        # Find max if we can place bomb there
                        if grid[i][j] != '0':
                            continue
                        answer = max(answer, row_count[i][j] + col_count[i][j])

                    count = 0
                    start = end + 1
                elif grid[i][end] == 'E':
                    count += 1

                end += 1

            # Process til end of row
            for j in range(start, end):
                row_count[i][j] = count

                # Find max if we can place bomb there
                if grid[i][j] != '0':
                    continue
                answer = max(answer, row_count[i][j] + col_count[i][j])

        return answer
    
test_cases = [
    [3, [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]],
    [1, [["W","W","W"],["0","0","0"],["E","E","E"]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.maxKilledEnemies(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")