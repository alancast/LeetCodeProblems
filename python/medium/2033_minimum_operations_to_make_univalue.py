from typing import List


class Solution:
    # flatten the grid, sort it, take middle
    # If any mod is different return -1 otherwise add different divisor
    # Time O(glogg) where g is n*m
    # Space O(g)
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened_grid = [num for row in grid for num in row]
        flattened_grid.sort()

        answer = 0
        # Take the middle number and move everything to it
        target_num = flattened_grid[len(flattened_grid)//2]
        target_mod = target_num % x

        for num in flattened_grid:
            # Make sure it's possible
            if num % x != target_mod:
                return -1
            
            answer += abs((target_num//x) - (num//x))

        return answer
    
test_cases = [
    [4, [[2,4],[6,8]], 2],
    [5, [[1,5],[2,3]], 1],
    [-1, [[1,2],[3,4]], 2]
]
solution = Solution()
for expected, grid, x in test_cases:
    actual = solution.minOperations(grid, x)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: grid: {grid}, x: {x}")

print("Ran all tests")