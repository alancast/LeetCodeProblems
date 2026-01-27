from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    # Djikstras with some added stuff
    # Time O(nlogn)
    # Space O(n)
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency graph
        graph = defaultdict(list)
        for source, dest, weight in edges:
            graph[source].append((dest, weight))
            # Also add the reverse one with double the weight
            # The shortest path will never cricket an edge so just add both
            graph[dest].append((source, 2*weight))

        visited = set()
        min_queue = []

        # Add starting values
        visited.add(0)
        for dest, weight in graph[0]:
            heappush(min_queue, (weight, dest))

        # Go djikstras until the end
        while min_queue:
            cost, node = heappop(min_queue)

            # Make sure not already visited then add to visited
            if node in visited:
                continue

            visited.add(node)

            # See if we've reached end state
            if node == n - 1:
                return cost

            # Add all the possible edges
            for dest, weight in graph[node]:
                heappush(min_queue, (cost + weight, dest))

        # Was not possible to get to node n-1
        return -1

test_cases = [
    [5, 4, [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]],
    [3, 4, [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]]
]
solution = Solution()
for expected, n, edges in test_cases:
    actual = solution.minCost(n, edges)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, edges: {edges}")

print("Ran all tests")
