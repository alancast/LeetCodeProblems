from collections import defaultdict, deque
from functools import cache


class Solution:
    MOD = 10**9 + 7

    # Lowest common ancestor then same math as before
    # Create graph, then find lowest common ancestor then do math
    # Time O(nlogn + qlogm)
    # Space O(nlogn)
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Create adjacency graph
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # Store each node for what level it is and who the parents is
        map = {}
        # Queue is in form (node, level, parent) tuples
        q = deque()
        q.append((1, 0, -1))
        while q:
            node, level, parent = q.popleft()
            map[node] = [level, parent]
            for neighbor in adj[node]:
                if neighbor != parent:
                    q.append((neighbor, level + 1, node))

        # Find lowest common ancestor of 2 nodes
        @cache
        def lca(a, b):
            while map[a][0] > map[b][0]:
                a = map[a][1]

            while map[a][0] < map[b][0]:
                b = map[b][1]

            while a != b:
                a = map[a][1]
                b = map[b][1]

            return a

        answer = []
        for a, b in queries:
            left = lca(a, b)
            levels = (map[a][0] - map[left][0]) + (map[b][0] - map[left][0])
            answer.append(0 if levels == 0 else pow(2, levels - 1, self.MOD))

        return answer

test_cases = [
    [[0,1], [[1,2]], [[1,1],[1,2]]],
    [[2,1,4], [[1,2],[1,3],[3,4],[3,5]], [[1,4],[3,4],[2,5]]]
]
solution = Solution()
for expected, edges, queries in test_cases:
    actual = solution.assignEdgeWeights(edges, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: edges: {edges} queries: {queries}")

print("Ran all tests")
