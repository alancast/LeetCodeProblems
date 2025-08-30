from typing import List


class Solution:
    # This doesn't actually check for valid sudokus, that is much harder
    # Think of case where first row is (.87654321) and the first col is (.23456789)
    # The number that goes in the top left has to be both 9 and 1, so that's invalid
    # But this would say it's valid
    # Create a hash set for rows, cols, and boxes
    # Go over whole board and make sure no dupes
    # Time O(n^2) as we go over whole n by n grid
    # Space O(n^2) as if grid is full we store all nums in 3 places
    # Space can be optimized by using bitmap instead of set
    # So each row col and box is just an int, and we do ands and ors
    # To set which nums we see. Which would just make space 3N
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]

                # If empty just skip
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box (boxes indexed 3* row//3 + col//3)
                box_index = (r // 3) * 3 + c // 3
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True

test_cases = [
    [True, [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]],
    [False, [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]]
]
solution = Solution()
for expected, board in test_cases:
    actual = solution.isValidSudoku(board)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: board: {board}")

print("Ran all tests")