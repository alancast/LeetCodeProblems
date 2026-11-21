class Solution:
    # DFS to find the size of each subtree, and keep track of the last node with the same letter on the path from the root to the current node.
    # Time O(n)
    # Space O(n)
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        children = [[] for _ in s]
        for x in range(1, len(s)):
            children[parent[x]].append(x)
        size, last = [1] * len(s), {}  # last[c]: the deepest node with letter c on the path from the root

        def dfs(x: int) -> None:
            c = s[x]
            above = last.get(c, -1)  # the closest ancestor with the same letter, or -1
            last[c] = x
            for child in children[x]:
                dfs(child)
            last[c] = above
            if x:  # the root has no parent
                size[above if above >= 0 else parent[x]] += size[x]

        dfs(0)
        return size

test_cases = [
    [[6, 3, 1, 1, 1, 1], [-1, 0, 0, 1, 1, 1], "abaabc"],
    [[5, 2, 1, 1, 1], [-1, 0, 4, 0, 1], "abbba"],
]
solution = Solution()
for expected, parent, s in test_cases:
    actual = solution.findSubtreeSizes(parent, s)
    if expected != actual:
                print(f"FAILED TEST! Expected {expected} but got {actual}")
                print(f"\tINPUTS: parent: {parent}, s: {s}")

print("Ran all tests")
