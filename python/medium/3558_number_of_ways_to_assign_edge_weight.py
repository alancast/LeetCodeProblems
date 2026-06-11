class Solution:
    MOD = 10**9 + 7

    # A combination of finding max depth, and then mathematics
    # First find the deepest depth, then just a simple math equation for that depth
    # Time O(n) for DFS
    # Space O(n) for graph and call stack
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1

        # Build the graph from the edges
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Find the max depth in the graph
        max_dep = self.dfs(graph, 1, 0)

        # Then just do the math of what the answer is
        return pow(2, max_dep - 1, self.MOD)

    # Time O(n) as we go over each node
    # Space O(n) for call stack
    def dfs(self, graph: list, starting_node: int, parent_node: int) -> int:
        max_dep = 0

        # Go over all the edges and find deepest depth
        for y in graph[starting_node]:
            # Don't go back up to parent (infinite loop then since undirected)
            if y == parent_node:
                continue

            max_dep = max(max_dep, self.dfs(graph, y, starting_node) + 1)

        return max_dep

test_cases = [
    [1, [[1,2]]],
    [2, [[1,2],[1,3],[3,4],[3,5]]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.assignEdgeWeights(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
