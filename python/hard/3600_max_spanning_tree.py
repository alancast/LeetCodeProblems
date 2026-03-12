# Disjoint union set class
class DSU:
    def __init__(self, parent):
        self.parent = parent

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.parent[px] = py


class Solution:
    # Spanning tree problem. Use disjoint union set
    # Time O(mlogm) m is length of edges
    # Space O(n+m)
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        answer = -1

        # What edges are required to be in the tree and which are optional
        must_edges = [e for e in edges if e[3] == 1]
        optional_edges = [e for e in edges if e[3] != 1]

        # If there aren't enough edges to connect the tree
        # Or if there are too many edges included than a cycle exists
        if len(edges) < n - 1 or len(must_edges) > n - 1:
            return -1

        # Sort by increasing edge weight
        optional_edges.sort(key=lambda x: x[2], reverse=True)

        # Start making the spanning tree
        selected_node = 0
        # A number bigger than edge range from problem
        must_min_stability = 10000000000
        starting_dsu = DSU(list(range(n)))

        # Add all the must edges to the spanning tree
        for u, v, s, _ in must_edges:
            # Make sure there isn't a cycle in the must edges
            if starting_dsu.find(u) == starting_dsu.find(v) or selected_node == n - 1:
                return -1
            starting_dsu.join(u, v)
            selected_node += 1
            must_min_stability = min(must_min_stability, s)

        # Do binary search to find min stability
        left = 0
        right = must_min_stability
        while left < right:
            mid = left + ((right - left + 1) >> 1)
            dsu = DSU(starting_dsu.parent[:])
            selected = selected_node
            doubledCount = 0

            for u, v, s, _ in optional_edges:
                # If they are already in the spanning tree ignore
                if dsu.find(u) == dsu.find(v):
                    continue

                # Try adding to the spanning tree
                if s >= mid:
                    dsu.join(u, v)
                    selected += 1
                elif doubledCount < k and s * 2 >= mid:
                    doubledCount += 1
                    dsu.join(u, v)
                    selected += 1
                else:
                    break

                # If added the last one then break
                if selected == n - 1:
                    break

            # See if we connected the whole tree or not and re-search
            if selected != n - 1:
                right = mid - 1
            else:
                answer = left = mid

        return answer

test_cases = [
    [2, 3, [[0,1,2,1],[1,2,3,0]], 1],
    [6, 3, [[0,1,4,0],[1,2,3,0],[0,2,1,0]], 2],
    [-1, 3, [[0,1,1,1],[1,2,1,1],[2,0,1,1]], 0]
]
solution = Solution()
for expected, n, edges, k in test_cases:
    actual = solution.maxStability(n, edges, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, edges: {edges}, k: {k}")

print("Ran all tests")
