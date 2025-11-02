from typing import List


class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    # Update visibility count for each cell after placing walls and guards
    # Time O(MxN)
    # Space O(MxN)
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        # Initialize grid as all unguarded
        grid = [[self.UNGUARDED] * n for _ in range(m)]

        # Mark guards' positions
        for row, col in guards:
            grid[row][col] = self.GUARD

        # Mark walls' positions
        for row, col in walls:
            grid[row][col] = self.WALL

        # Updates the visibility of a cell based on the current guard line state.
        def _update_cell_visibility(row: int, col: int, is_guard_line_active: bool) -> bool:
            # If current cell is a guard, reactivate the guard line
            if grid[row][col] == self.GUARD:
                return True

            # If current cell is a wall, deactivate the guard line
            if grid[row][col] == self.WALL:
                return False

            # If guard line is active, mark cell as guarded
            if is_guard_line_active:
                grid[row][col] = self.GUARDED

            return is_guard_line_active

        # Horizontal passes
        for row in range(m):
            is_guard_line_active = grid[row][0] == self.GUARD
            for col in range(1, n):
                is_guard_line_active = _update_cell_visibility(
                    row, col, is_guard_line_active
                )
            is_guard_line_active = grid[row][n - 1] == self.GUARD
            for col in range(n - 2, -1, -1):
                is_guard_line_active = _update_cell_visibility(
                    row, col, is_guard_line_active
                )

        # Vertical passes
        for col in range(n):
            is_guard_line_active = grid[0][col] == self.GUARD
            for row in range(1, m):
                is_guard_line_active = _update_cell_visibility(
                    row, col, is_guard_line_active
                )
            is_guard_line_active = grid[m - 1][col] == self.GUARD
            for row in range(m - 2, -1, -1):
                is_guard_line_active = _update_cell_visibility(
                    row, col, is_guard_line_active
                )

        # Go over whole grid and count unguarded cells
        answer = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == self.UNGUARDED:
                    answer += 1

        return answer

    # Too slow
    # When you see a guard go in all directions and mark as guarded
    # Then go over all cells again and count unguarded
    # Time O(MxN)
    # Space O(MxN)
    def countUnguarded_simulation(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Create grid
        grid = [['F'] * n for _ in range(m)]

        # Go through and add walls
        for wall in walls:
            grid[wall[0]][wall[1]] = 'W'
        
        # Go over all guards
        for guard in guards:
            row = guard[0]
            col = guard[1]

            # Make sure this cell is guarded
            grid[row][col] = 'G'
            # Make sure all down until wall are guarded
            temp_row = row + 1
            while temp_row < m:
                if grid[temp_row][col] == 'W':
                    break

                # Mark square as seen
                grid[temp_row][col] = 'S'
                temp_row += 1

            # Make sure all up until wall are guarded
            temp_row = row - 1
            while temp_row >= 0:
                if grid[temp_row][col] == 'W':
                    break

                # Mark square as seen
                grid[temp_row][col] = 'S'
                temp_row -= 1

            # Make sure all right until wall are guarded
            temp_col = col + 1
            while temp_col < n:
                if grid[row][temp_col] == 'W':
                    break

                # Mark square as seen
                grid[row][temp_col] = 'S'
                temp_col += 1

            # Make sure all left until wall are guarded
            temp_col = col - 1
            while temp_col >= 0:
                if grid[row][temp_col] == 'W':
                    break

                # Mark square as seen
                grid[row][temp_col] = 'S'
                temp_col -= 1

        # Go over all spaces and count all unguarded
        answer = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 'F':
                    answer += 1

        return answer

test_cases = [
    [7, 4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]],
    [4, 3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]]
]
solution = Solution()
for expected, m, n, guards, walls in test_cases:
    actual = solution.countUnguarded(m, n, guards, walls)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: m: {m}, n: {n}, guards: {guards}, walls: {walls}")

print("Ran all tests")