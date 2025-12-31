from typing import List


class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]


class Solution:
    # Disjoint set similar to below but do it on water
    # Find last day water doesn't connect left to right
    # Time O(row * col)
    # Space O(row * col)
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col + 2
        root = list(range(n))

        # Disjoint set functions
        def find(x: int) -> int:
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        def union(x: int, y: int):
            rx, ry = find(x), find(y)
            if rx < ry:
                root[ry] = rx
            elif ry < rx:
                root[rx] = ry

        # Since water can connect diagonally there are more directions now
        directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        # Initialize everything to land
        grid = [[0] * col for _ in range(row)]
        left = 0
        right = n-1
        day = 0

        # Go over all cells until water is connected left to right
        for r, c in cells:
            # Since things are 1 indexed subtract 1
            r = r-1
            c = c-1

            # Make this cell water
            grid[r][c] = 1
            # Compute index in the array
            curr_idx = r*col+c+1
            # See if this connects with any water
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc

                # See if there is any nearby water to join with
                if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] == 1:
                    union(curr_idx, new_row*col+new_col+1)

            # See if water touches left (if so union)
            if c == 0:
                union(curr_idx, left)
            # See if water touches right (if so union)
            if c == col-1:
                union(curr_idx, right)
            # See if we now have connected left and right, if so break
            if find(left) == find(right):
                break

            # Increment day by 1 and go to next cell
            day += 1
        
        # Broken out of loop with final day they connected
        return day

    # Disjoint set go until there are no land sets that touch both top and bottom
    # Could have also done with binary search and then bfs (or dfs)
    # Binary search to see if it's still doable on day x, if so or not adjust
    # Find last way doable that way. That would be logc * row * col
    # Time O(row * col)
    # Space O(row * col)
    def latestDayToCross_dsu_land(self, row: int, col: int, cells: List[List[int]]) -> int:
        # Create disjoint set add 2, one for top row one for bottom
        dsu = DSU(row * col + 2)
        # Initialize everything to water as we are going backwards
        grid = [[1] * col for _ in range(row)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Go over all cells in reverse order
        # Reverse order is because we are looking for first set that
        # Touches top and bottom (as that's the last day it's possible)
        for i in range(len(cells) - 1, -1, -1):
            r = cells[i][0] - 1
            c = cells[i][1] - 1
            grid[r][c] = 0
            index_1 = r * col + c + 1
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                new_index = new_row * col + new_col + 1
                # Make sure new index is in range and is land, join sets
                if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] == 0:
                    dsu.union(index_1, new_index)

            # If top row make sure it's known it touches top
            if r == 0:
                dsu.union(0, index_1)
            # If bottom row make sure it's known it touches bottom
            if r == row - 1:
                dsu.union(row * col + 1, index_1)
            # See if top row and bottom row are now same set, if so we have answer
            if dsu.find(0) == dsu.find(row * col + 1):
                return i
        
        # This will never happen as input guarantees water blocks it eventually
        return -1

test_cases = [
    [2, 2, 2, [[1,1],[2,1],[1,2],[2,2]]],
    [1, 2, 2, [[1,1],[1,2],[2,1],[2,2]]],
    [3, 3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]]
]
solution = Solution()
for expected, row, col, cells in test_cases:
    actual = solution.latestDayToCross(row, col, cells)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: row: {row}, col: {col}, cells: {cells}")

print("Ran all tests")
