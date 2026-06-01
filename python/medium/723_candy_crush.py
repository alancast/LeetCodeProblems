class Solution:
    # Just go through the simulation time after time
    # Find and crush then drop, repeat until nothing else found
    # Time O(m^2 + n^2)
    # Space O(1) modify in place
    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        rows = len(board)
        cols = len(board[0])

        # Finds any valid groups of 3 or more
        # Returns True if found things to crush, False if none
        # Modifies board
        def find_and_crush() -> bool:
            found_group = False

            # Check for vertical groups
            for row in range(rows - 2):
                for col in range(cols):
                    # Nothing there so carry on
                    if board[row][col] == 0:
                        continue

                    # Check abs because we in place swap to negative to mark crushed
                    if abs(board[row][col]) == abs(board[row + 1][col]) == abs(board[row + 2][col]):
                        board[row][col] = -abs(board[row][col])
                        board[row + 1][col] = -abs(board[row + 1][col])
                        board[row + 2][col] = -abs(board[row + 2][col])

                        # Make sure to set that we found a group to crush
                        found_group = True

            # Check for horizontal groups
            for row in range(rows):
                for col in range(cols - 2):
                    # Nothing there so carry on
                    if board[row][col] == 0:
                        continue

                    # Check abs because we in place swap to negative to mark crushed
                    if abs(board[row][col]) == abs(board[row][col + 1]) == abs(board[row][col + 2]):
                        board[row][col] = -abs(board[row][col])
                        board[row][col + 1] = -abs(board[row][col + 1])
                        board[row][col + 2] = -abs(board[row][col + 2])

                        # Make sure to set that we found a group to crush
                        found_group = True

            # Set the value of each candies to be crushed as 0
            for row in range(rows):
                for col in range(cols):
                    board[row][col] = max(board[row][col], 0)

            return found_group

        # Modifies board. Drops everything down
        def drop():
            for col in range(cols):
                lowest_zero = -1

                # Iterate over each column from last row to top
                for row in range(rows - 1, -1, -1):
                    # If we see a 0 update lowest 0
                    if board[row][col] == 0:
                        lowest_zero = max(lowest_zero, row)
                        continue

                    # Found a non zero to swap but make sure we have a 0 below it to swap with
                    if lowest_zero >= 0:
                        # Swap current non-zero candy with the lowest zero.
                        board[row][col], board[lowest_zero][col] = board[lowest_zero][col], board[row][col]

                        # Move the zero up a spot
                        lowest_zero -= 1

        # Continue with the three steps until we can no longer find any crushable candies.
        while find_and_crush():
            drop()

        return board

test_cases = [
    [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]], [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]],
    [[[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]], [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]]
]
solution = Solution()
for expected, board in test_cases:
    actual = solution.candyCrush(board)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: board: {board}")

print("Ran all tests")
