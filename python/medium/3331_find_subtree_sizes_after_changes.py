class Solution:
    # First build the children of each node so we can traverse the original tree
    # Then find the closest matching ancestor for each node during the traversal
    # Time O(n)
    # Space O(n)
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        # Store the children using the original parent array
        children = [[] for _ in s]
        for x in range(1, len(s)):
            children[parent[x]].append(x)

        # Every node starts with a subtree size of 1
        # last stores the deepest node with each letter on the current path
        size, last = [1] * len(s), {}

        def dfs(x: int) -> None:
            c = s[x]

            # Save the closest matching ancestor, or -1 if there isn't one
            above = last.get(c, -1)

            # Make this node the closest matching ancestor for its descendants
            last[c] = x

            # Visit the original children to compute their final subtree sizes
            for child in children[x]:
                dfs(child)

            # Restore the previous matching ancestor for the next branch
            last[c] = above

            # Add this subtree to its new parent, or its original parent if no match
            if x:
                size[above if above >= 0 else parent[x]] += size[x]

        # Start at the root and return the final subtree sizes
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
