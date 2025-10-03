from typing import List


class Solution:
    # Disjoint Set and greedy addition of edges to find minimum spanning tree
    # Sort edges by lowest cost, then greedily add edges that make set bigger
    # Go until set is of size N (would be more efficient but not done here)
    # Here we go through all edges and then pick city at end and find root
    # Then go through all N cities and make sure all have same root
    # Time O(MlogM + MlogN + N) for sorting M connections then everything else
    # Space O(N)
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # Find what set the city is in
        def find(city: int) -> int:
            # Recursively re-set city's parent to its parent's parent.
            if parent[city] != city:
                parent[city] = find(parent[city])

            return parent[city]
        
        # Union the two cities into the same set
        def union(city_1: int, city_2: int) -> bool:
            # Find the set the cities are in
            root_1 = find(city_1)
            root_2 = find(city_2)

            # Already in the same set so don't join
            if root_1 == root_2:
                return False

            # Join the sets (doesn't really matter which way, more efficient if smaller)
            parent[root_2] = root_1

            # Successful union
            return True
        
        # Keep track of disjoint sets. Initially each city is its own set.
        # This could be it's own DisjointSet class too but didn't want to implement today
        parent = {city: city for city in range(1, n+1)}

        # Sort connections so we are always picking minimum cost edge.
        connections.sort(key=lambda x: x[2])

        # Go over all connections and greedily add all that union multiple sets together
        total = 0
        for city1, city2, cost in connections:
            # If union here is false they are already the same set so don't add edge
            if union(city1, city2):
                total += cost

        # Check that all cities are connected.
        root = find(n)

        # Make sure all cities have the same set (root). Could also go by size
        return total if all(root == find(city) for city in range(1, n+1)) else -1

test_cases = [
    [6, 3, [[1,2,5],[1,3,6],[2,3,1]]],
    [-1, 4, [[1,2,3],[3,4,4]]]
]
solution = Solution()
for expected, n, connections in test_cases:
    actual = solution.minimumCost(n, connections)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, connections: {connections}")

print("Ran all tests")