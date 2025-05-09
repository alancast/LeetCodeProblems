from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class SearchState:
    distance: int
    node: int

    def __init__(self, node: int, distance: int):
        self.node = node
        self.distance = distance

    def __lt__(self, other) -> bool:
        return self.distance < other.distance


# Djikstra is the best and fastest and most intuitive answer here
# But good practice and learning on Bellman-Ford and ShortestPathFaster algorithms
class Solution:
    # Use ShortestPathFaster algorithm
    # n is number of nodes m is number of edges
    # Time O(n * m) go through potentially every edge n-1 times
    # Space O(n + m) distance array and edges dict
    def minimumDistance(self, n: int, edges: list[list[int]], s: int, marked: list[int]) -> int:
        # Initialize distances array with maximum values
        dist = [float("inf")] * n
        dist[s] = 0
        # Dict of source to list of destinations with weight
        edges_dict = defaultdict(list[tuple])

        # Precompute edges dict
        for source, target, weight in edges:
            edges_dict[source].append((target, weight))

        # Bellman-Ford algorithm but only for updated nodes
        updated_nodes_set = set({s})
        for _ in range(n - 1):
            # No nodes were updated so we can break out of loop
            if len(updated_nodes_set) == 0:
                break

            next_updated = set()
            # See if any of the updated nodes can shorten any future nodes
            for node in updated_nodes_set:
                for target, weight in edges_dict[node]:
                    if dist[node] + weight < dist[target]:
                        dist[target] = dist[node] + weight
                        next_updated.add(target)

            updated_nodes_set = next_updated

        # Find minimum distance to any marked node
        min_dist = float("inf")
        for node in marked:
            min_dist = min(min_dist, dist[node])

        # Return -1 if no path exists, otherwise return the minimum distance
        if min_dist == float("inf"):
            return -1
        
        return min_dist

    # Use Bellman-Ford algorithm
    # n is number of nodes m is number of edges
    # Time O(n * m) go through every edge n-1 times
    # Space O(n) just distance array
    def _minimum_distance_bellman_ford(self, n: int, edges: list[list[int]], s: int, marked: list[int]) -> int:
        # Initialize distances array with maximum values
        dist = [float("inf")] * n
        dist[s] = 0

        # Bellman-Ford algorithm: relax edges n-1 times
        for _ in range(n - 1):
            for from_node, to_node, weight in edges:
                # Relaxation step: if we can improve the path to 'to_node' via 'from_node'
                if dist[from_node] != float("inf") and dist[from_node] + weight < dist[to_node]:
                    dist[to_node] = dist[from_node] + weight

        # Find minimum distance to any marked node
        min_dist = float("inf")
        for node in marked:
            min_dist = min(min_dist, dist[node])

        # Return -1 if no path exists, otherwise return the minimum distance
        if min_dist == float("inf"):
            return -1
        
        return min_dist

    # Use djikstras search
    # n is number of nodes m is number of edges
    # Time O(n + mlogm) n because create visited set of size n mlogm for search and heap push
    # Space O(n + m) m for search queue
    def _minimum_distance_djikstras(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        marked_set = set(marked)
        visited = [False] * n
        # Dict of source to list of destinations with weight
        edges_dict = defaultdict(list[tuple])

        # Precompute edges dict
        for edge in edges:
            source = edge[0]
            target = edge[1]
            weight = edge[2]
            edges_dict[source].append((target, weight))

        # Do djikstras
        min_heap = [SearchState(s, 0)]
        while min_heap:
            search_state: SearchState = heappop(min_heap)
            node = search_state.node
            distance = search_state.distance

            # See if this is a marked node and end
            if node in marked_set:
                return distance

            # See if node was visited earlier by shorter route
            if visited[node]:
                continue

            # Mark node as visited
            visited[node] = True

            # Add all it's edges to the heap
            for target, weight in edges_dict[node]:
                heappush(min_heap, SearchState(target, distance + weight))

        return -1
    
test_cases = [
    [4, 4, [[0,1,1],[1,2,3],[2,3,2],[0,3,4]], 0, [2,3]],
    [3, 5, [[0,1,2],[0,2,4],[1,3,1],[2,3,3],[3,4,2]], 1, [0,4]],
    [-1, 4, [[0,1,1],[1,2,3],[2,3,2]], 3, [0,1]]
]
solution = Solution()
for expected, n, edges, s, marked in test_cases:
    actual = solution.minimumDistance(n, edges, s, marked)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, edges: {edges}, s: {s}, marked: {marked}")

print("Ran all tests")