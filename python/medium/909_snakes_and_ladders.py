from collections import deque
from typing import List


class Solution:
    # DP where you store in the array how many moves to get there
    # Queue of updated squares to go through
    # Time O(n^2) as worst case we go through the whole grid
    # Space O(n^2) as we store the dp array
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.n = len(board)
        n_squared = self.n * self.n

        # +1 because it's one indexed
        moves_from_end = [-1] * (n_squared + 1)
        moves_from_end[1] = 0

        new_spaces = deque()
        new_spaces.appendleft(1)

        while new_spaces:
            i = new_spaces.popleft()
            current_moves = moves_from_end[i]

            # Update dice roll values
            for rolled_to in range(i + 1, min(i + 6, n_squared) + 1):
                roll_row, roll_col = self._get_row_col_from_index(rolled_to)

                # If there is a snake or ladder we must take it
                destination = board[roll_row][roll_col]
                if destination == -1:
                    destination = rolled_to

                # See if reached end
                if destination == n_squared:
                    return current_moves + 1

                if moves_from_end[destination] == -1:
                    moves_from_end[destination] = current_moves + 1
                    new_spaces.append(destination)

        return moves_from_end[-1]
    
    def _get_row_col_from_index(self, index: int) -> tuple:
        row = self.n - ((index-1)//self.n) - 1
        col = (index-1) % self.n
        # See if col number needs to change based on counting backwards
        if ((index-1)//self.n) % 2 == 1:
            col = self.n - 1 - ((index - 1) % self.n)

        return (row, col)

    
test_cases = [
    [4, [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]],
    [1, [[-1,-1],[-1,3]]],
    [-1, [[1,1,-1],[1,1,1],[-1,1,1]]],
    [3, [[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]]],
    [4, [[-1,-1,27,13,-1,25,-1],[-1,-1,-1,-1,-1,-1,-1],[44,-1,8,-1,-1,2,-1],[-1,30,-1,-1,-1,-1,-1],[3,-1,20,-1,46,6,-1],[-1,-1,-1,-1,-1,-1,29],[-1,29,21,33,-1,-1,-1]]]
]
solution = Solution()
for expected, board in test_cases:
    actual = solution.snakesAndLadders(board)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: board: {board}")

print("Ran all tests")