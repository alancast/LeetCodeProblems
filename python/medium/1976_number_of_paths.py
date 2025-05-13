from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    MOD = 10**9 + 7

    # Djikstras algorithm
    # Time O(n + rlogr) n for creating structures rlogr for djikstras
    # Space O(n + r)
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Create dependency graph
        dependency_graph = defaultdict(list[int])
        for source, destination, time in roads:
            dependency_graph[source].append((destination, time))
            dependency_graph[destination].append((source, time))
        
        # Create path counts array for how many different ways there are to get to a node
        path_counts = [0] * n
        path_counts[0] = 1
        # Create shortest_time array for shortest time to each node
        shortest_time = [float("inf")] * n
        
        current_time = 0
        djikstras: List[tuple] = []
        heappush(djikstras, (0,0))
        while djikstras:
            current_time, source_node = heappop(djikstras)
            # Skip outdated distances
            if current_time > shortest_time[source_node]:
                continue

            for destination, time in dependency_graph[source_node]:
                # Found a new shortest path → Update shortest time and reset path count
                if current_time + time < shortest_time[destination]:
                    shortest_time[destination] = current_time + time
                    path_counts[destination] = path_counts[source_node]
                    heappush(djikstras, (shortest_time[destination], destination))
                elif current_time + time == shortest_time[destination]:
                    path_counts[destination] += path_counts[source_node]
                    path_counts[destination] %= self.MOD
        
        return path_counts[-1]
    
test_cases = [
    [4, 7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]],
    [1, 2, [[1,0,10]]]
]
solution = Solution()
for expected, n, roads in test_cases:
    actual = solution.countPaths(n, roads)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, roads: {roads}")

print("Ran all tests")