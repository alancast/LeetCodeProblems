from typing import List


class Solution:
    # Try numbers and backtrack if it doesn't work
    # Time O((9!)^9) so freaking massive
    # Space O(81)
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # List of indices (row, column)
        empties = []

        # Initialize sets with existing numbers
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    empties.append((row, col))
                else:
                    num = board[row][col]
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[((row//3)*3) + (col//3)].add(num)

        def dfs(idx=0):
            # If filled all empty cells sudoku is solved
            if idx == len(empties):
                return True

            row, col = empties[idx]
            box = ((row//3)*3) + (col//3)

            for num in '123456789':
                if num not in rows[row] and num not in cols[col] and num not in boxes[box]:
                    # Place num
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

                    # Go to next index in list and try placing it
                    if dfs(idx+1):
                        return True

                    # Backtrack and try next num
                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box].remove(num)

            # Got through all nums, board not solvable in this state
            return False

        dfs()
