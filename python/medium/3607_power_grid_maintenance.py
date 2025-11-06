from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class DisjointSetUnionMinimal:
    parents: List[int]

    def __init__(self, n: int):
        self.parents = [i for i in range(n)]

    def find(self, node1: int) -> int:
        if node1 != self.parents[node1]:
            self.parents[node1] = self.find(self.parents[node1])

        return self.parents[node1]

    def union(self, node1: int, node2: int) -> None:
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        # Merge parents together (smaller takes priority)
        if parent1 != parent2:
            if parent1 < parent2:
                self.parents[parent2] = parent1
            else:
                self.parents[parent1] = parent2


class DisjointSetUnion:
    parent: List[int]
    is_online: List[bool]
    lowest_online: List[List[int]]

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]

        # Initially all are online and lowest is self
        self.is_online = [True for _ in range(n)]
        self.lowest_online = [[i] for i in range(n)]

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            node = self.parent[node]

        return node
    
    def union(self, node1: int, node2: int) -> None:
        p1 = self.find(node1)
        p2 = self.find(node2)
        
        # Always merge p2 with p1 return weight of walk
        self.parent[p2] = p1
        # Go through all of P2's onlines and add them into p1
        while self.lowest_online[p2]:
            heappush(self.lowest_online[p1], self.lowest_online[p2][-1])
            self.lowest_online[p2].pop(-1)
    
    def get_online(self, node1: int) -> int:
        # If this node is online return itself
        if self.is_online[node1]:
            return node1

        # If it's not online get the lowest online one in it's grid
        p1 = self.find(node1)
        # Nothing online in this set
        if not self.lowest_online[p1]:
            return -1
        
        # Return lowest online ID
        return self.lowest_online[p1][0]
    
    def take_offline(self, node1: int) -> None:
        # If it's already offline do nothing
        if not self.is_online[node1]:
            return

        # Take this offline
        self.is_online[node1] = False

        # Find what set this is in and make sure it's taken offline there too
        p1 = self.find(node1)

        # Remove it from the online array of that set
        self.lowest_online[p1].remove(node1)

class Solution:
    # The same logic as the one below, just faster as process heap less
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Create sets
        dsjm = DisjointSetUnionMinimal(c+1)
        for u, v in connections:
            dsjm.union(u, v)
        
        # Populate a list of minimum power ids in sets
        min_in_component = defaultdict(list)
        for i in range(c+1):
            heappush(min_in_component[dsjm.find(i)], i)
     
        online_status = [True] * (c+1)
        answer = []

        # Go over all query types and process them
        for query_type, station in queries:
            # If taking something offline do that
            if query_type == 2:
                online_status[station] = False
            # If looking for min online thing in component
            else:
                # If this is online just return it
                if online_status[station]:
                    answer.append(station)
                # If it's not, search for min, but remember we didn't purge
                # So will need to fact check that it's still online
                else:
                    # Get the heap of min online components for this set
                    min_in_component_heap = min_in_component[dsjm.find(station)]
                    not_found = True
                    # Go through heap and check until finding min still online
                    # If not still online, pop and find next
                    while min_in_component_heap:
                        station = min_in_component_heap[0]
                        # If the min is still online we have our answer
                        if online_status[station]:
                            answer.append(station)
                            not_found = False
                            break
                        # The min wasn't still online so pop it and try next
                        heappop(min_in_component_heap)
                    # We didn't find anything still online in this component
                    if not_found:
                        answer.append(-1)
        
        return answer

    # A disjoint set union of the grids where when they join the lowest ID is parent
    # Then process queries by doing find
    # Time O(nlogn + qlogn) for joining connections sets and queries
    # Space O(n)
    def processQueries_slow(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Create union find (add 1 because 1 indexed)
        dsj = DisjointSetUnion(c+1)

        # Go over all connections and join unions
        for node1, node2 in connections:
            dsj.union(node1, node2)
        
        # Go over all queries and get answers
        answer = []
        for query_type, station in queries:
            if query_type == 2:
                dsj.take_offline(station)
            else:
                answer.append(dsj.get_online(station))

        return answer

test_cases = [
    [[3,2,3], 5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]]],
    [[1,-1], 3, [], [[1,1],[2,1],[1,1]]]
]
solution = Solution()
for expected, c, connections, queries in test_cases:
    actual = solution.processQueries(c, connections, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: c: {c}, connections: {connections}, queries: {queries}")

print("Ran all tests")