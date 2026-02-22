from collections import defaultdict, deque


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        while self.par[node] != node:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


class Solution:
    # Time O(n + E * n) n for creating union find E * n for edges union find
    # Space O(N + E)
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        components = n
        uf = UnionFind(n)

        # Go through all edges, and every time there is edges that are in same component
        # Subtract components
        for source, destination in edges:
            if uf.union(source,destination):
                components -= 1

        return components

    # Time O(n + E)
    # Space O(n + E) as we create edges map and visited array
    def countComponents_bfs(self, n: int, edges: list[list[int]]) -> int:
        visited_arr = [False] * n

        # Create adjacency graph
        adjacency_map = defaultdict(list[int])
        for source, target in edges:
            adjacency_map[source].append(target)
            adjacency_map[target].append(source)

        component_count = 0
        # Iterate over visited map and do breadth first search each time we see a not visited one
        for i, visited in enumerate(visited_arr):
            if visited:
                continue

            component_count += 1
            visited_arr[i] = True
            # Do bfs now from i
            q = deque()
            q.append(i)
            while q:
                node = q.popleft()
                visited_arr[node] = True
                for dest in adjacency_map[node]:
                    if not visited_arr[dest]:
                        q.append(dest)

        return component_count

test_cases = [
    [2, 5, [[0,1],[1,2],[3,4]]],
    [1, 5, [[0,1],[1,2],[2,3],[3,4]]],
    [1, 2, [[1,0]]]
]
solution = Solution()
for expected, n, edges in test_cases:
    actual = solution.countComponents(n, edges)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}, edges: {edges}")

print("Ran all tests")
