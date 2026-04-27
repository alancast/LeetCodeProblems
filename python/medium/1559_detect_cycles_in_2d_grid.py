class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.setCount = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find_set(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int):
        # Always merge smaller into bigger
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1

    def findAndUnite(self, x: int, y: int) -> bool:
        parent_x = self.find_set(x)
        parent_y = self.find_set(y)

        if parent_x != parent_y:
            self.unite(parent_x, parent_y)
            return True

        # They were already in the same set
        return False


class Solution:
    # Use union find to try to find cycles
    # Time O(mn * UF)
    # Space O(mn)
    def containsCycle(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m * n)

        for i in range(m):
            for j in range(n):
                # If they are already in the same set it's a cycle
                if (i > 0 and
                    grid[i][j] == grid[i - 1][j] and
                    not uf.findAndUnite((i * n) + j, ((i - 1) * n) + j)
                ):
                    return True
                if (j > 0 and
                    grid[i][j] == grid[i][j - 1] and
                    not uf.findAndUnite((i * n) + j, (i * n) + j - 1)
                ):
                    return True

        return False

test_cases = [
    [True, [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]],
    [True, [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]],
    [False, [["a","b","b"],["b","z","b"],["b","b","a"]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.containsCycle(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
