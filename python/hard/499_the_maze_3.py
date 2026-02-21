from heapq import heappop, heappush


class Solution:
    # Dijkstra's just with a lot of stuff
    # Time O(nlogn) where n is total squares in the maze
    # Space O(n)
    def findShortestWay(self, maze: list[list[int]], ball: list[int], hole: list[int]) -> str:
        rows = len(maze)
        cols = len(maze[0])

        # Returns true if row col is valid in maze, false if not
        def valid(row: int, col: int) -> bool:
            return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0

        # Returns the neighbor if you go left, up, right, then down
        def get_neighbors(row: int, col: int) -> list[tuple]:
            directions = [(0, -1, 'l'), (-1, 0, 'u'), (0, 1, 'r'), (1, 0, 'd')]
            neighbors = []

            # Go over all directions
            for dy, dx, direction in directions:
                curr_row = row
                curr_col = col
                dist = 0

                # Keep moving in that direction until you hit a wall or the hole
                while valid(curr_row + dy, curr_col + dx):
                    curr_row += dy
                    curr_col += dx
                    dist += 1

                    # See if we have found the hole
                    if [curr_row, curr_col] == hole:
                        break

                # Append the neighbor in that direction
                neighbors.append((curr_row, curr_col, dist, direction))

            return neighbors

        # Heap stores (total dist, path, current row, current col)
        heap = [(0, "", ball[0], ball[1])]
        # What row, col combinations have ew already examined
        seen = set()

        # Do Dijkstra's until hole is found or all spaces seen
        while heap:
            curr_dist, path, row, col = heappop(heap)

            # Already processed this node
            if (row, col) in seen:
                continue

            # Found shortest way out so return path
            if [row, col] == hole:
                return path

            # Add this entry to what we've already examined
            seen.add((row, col))

            # Get all the neighbor in the left, up, right, and down directions
            for next_row, next_col, dist, direction in get_neighbors(row, col):
                # Add this to the queue
                heappush(heap, (curr_dist + dist, path + direction, next_row, next_col))

        # Went through every possibility and none were possible
        return "impossible"

test_cases = [
    ["lul", [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1]],
    ["impossible", [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [3,0]],
    ["dldr", [[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]], [0,4], [3,5]]
]
solution = Solution()
for expected, maze, ball, hole in test_cases:
    actual = solution.findShortestWay(maze, ball, hole)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: maze: {maze}, ball: {ball}, hole: {hole}")

print("Ran all tests")
