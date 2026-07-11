from collections import defaultdict


class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1] * n
        self.size = [1] * n

    # Find root of component with path compression
    def _find(self, node: int) -> int:
        if self.parent[node] == -1:
            return node

        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]

    # Union by size always merge smaller into larger one
    def _union(self, node_1: int, node_2: int) -> None:
        root_1 = self._find(node_1)
        root_2 = self._find(node_2)

        if root_1 == root_2:
            return

        # Merge smaller component into larger one
        if self.size[root_1] > self.size[root_2]:
            self.parent[root_2] = root_1
            self.size[root_1] += self.size[root_2]
        else:
            self.parent[root_1] = root_2
            self.size[root_2] += self.size[root_1]

class Solution:
    # Union find and store edge count (also implemented this a second time in this repo I guess)
    # Time O(n + e)
    # Space O(n)
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Initialize Union Find and edge counter
        dsu = UnionFind(n)
        edge_count = defaultdict(int)

        # Connect components using edges
        for edge in edges:
            dsu._union(edge[0], edge[1])

        # Count edges in each component
        for edge in edges:
            root = dsu._find(edge[0])
            edge_count[root] += 1

        # Check if each component is complete
        complete_count = 0
        for vertex in range(n):
            # Make sure vertex is root of it's component
            if dsu._find(vertex) == vertex:
                node_count = dsu.size[vertex]
                # See how many edges the component should have to be completely connected
                expected_edges = (node_count * (node_count - 1)) // 2
                if edge_count[vertex] == expected_edges:
                    complete_count += 1

        return complete_count

test_cases = [
    [3, 6, [[0,1],[0,2],[1,2],[3,4]]],
    [1, 6, [[0,1],[0,2],[1,2],[3,4],[3,5]]]
]
solution = Solution()
for expected, n, edges in test_cases:
    actual = solution.countCompleteComponents(n, edges)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, edges: {edges}")

print("Ran all tests")
