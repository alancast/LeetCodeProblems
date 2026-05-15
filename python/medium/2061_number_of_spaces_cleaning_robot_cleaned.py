class Solution:
    # Keep visited set and just go until you've visited a cell in that direction before
    # Time O(mn) as robot just goes to each space once
    # Space O(mn) to keep visited set
    # Could improve space my modifying room to be set to direction it was visited in
    # E.g. add 2 for up, 4 for right, 8 for left, 16 for down and bitwise to check
    def numberOfCleanRooms(self, room: list[list[int]]) -> int:
        rows = len(room)
        cols = len(room[0])

        # 0 is moving right, 1 is down, 2 is left, 3 is up
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = {}
        cleaned = 0
        dir_idx = 0
        curr_row = curr_col = 0

        # Go until we've already visited this square in this direction
        while (curr_row, curr_col) not in visited or dir_idx not in visited[(curr_row, curr_col)]:
            # See if this cell has already been cleaned, if not clean it
            if (curr_row, curr_col) not in visited:
                cleaned += 1
                visited[(curr_row, curr_col)] = set()

            # Add to visited
            visited[(curr_row, curr_col)].add(dir_idx)

            # Compute next cell (handle turning)
            found_move = False
            next_dir_idx = next_row = next_col = 0
            for i in range(4):
                next_dir_idx = (dir_idx + i) % 4
                next_row = curr_row + directions[next_dir_idx][0]
                next_col = curr_col + directions[next_dir_idx][1]

                if next_row >=0 and next_row < rows and next_col >= 0 and next_col < cols and room[next_row][next_col] != 1:
                    found_move = True
                    break

            # There was no where to go, so break out
            if not found_move:
                break

            curr_row = next_row
            curr_col = next_col
            dir_idx = next_dir_idx

        return cleaned

test_cases = [
    [7, [[0,0,0],[1,1,0],[0,0,0]]],
    [1, [[0,1,0],[1,0,0],[0,0,0]]],
    [8, [[0,0,0],[0,0,0],[0,0,0]]]
]
solution = Solution()
for expected, room in test_cases:
    actual = solution.numberOfCleanRooms(room)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: room: {room}")

print("Ran all tests")
