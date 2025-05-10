from collections import defaultdict, deque
from typing import List


class UnionFind:
    parent: List[int]
    weight: List[int]

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        # -1 has only 1s in its binary representation
        self.weight = [-1] * n

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            node = self.parent[node]

        return node
    
    def union(self, node1: int, node2: int, weight: int) -> int:
        p1 = self.find(node1)
        p2 = self.find(node2)
        
        # Always merge p2 with p1 return weight of walk
        self.parent[p2] = p1
        self.weight[p1] = self.weight[p1] & weight & self.weight[p2]

        return self.weight[p1]
    
    def get_cost(self, node1: int, node2: int) -> int:
        p1 = self.find(node1)
        p2 = self.find(node2)

        if p1 != p2:
            return -1
        
        return self.weight[p1]

class Solution:
    # Use BFS to find all the components and their walk cost. Then go over queries
    # Time O(V*N+Q)
    # Space O(V+N)
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Create the adjacency graph
        adj_map = defaultdict(list[tuple])
        for source, dest, weight in edges:
            adj_map[source].append((dest,weight))
            adj_map[dest].append((source,weight))

        visited = [False] * n

        # Array to store the component ID of each node
        components = [0] * n
        component_cost = []

        component_id = 0

        # Perform BFS for each unvisited node to identify components and calculate their costs
        for node in range(n):
            if not visited[node]:
                # Get the component cost and mark all nodes in the component
                cost = self._get_component_cost(node, adj_map, visited, components, component_id)
                component_cost.append(cost)
                component_id += 1

        # Get answer of all queries
        answer = []
        for start, end in query:
            if components[start] == components[end]:
                # If they are in the same component, return the precomputed cost for the component
                answer.append(component_cost[components[start]])
            else:
                # If they are in different components, return -1
                answer.append(-1)

        return answer

    # Helper function to calculate the cost of a component using BFS
    def _get_component_cost(
        self, source: int, adj_map: dict, visited: List[int], 
        components: List[int], component_id: int
    ):
        nodes_queue = deque()

        # Initialize the component cost to the number that has only 1s in its binary representation
        component_cost = -1

        nodes_queue.append(source)
        visited[source] = True

        # Perform BFS to explore the component and calculate the cost
        while nodes_queue:
            node = nodes_queue.popleft()

            # Mark the node as part of the current component
            components[node] = component_id

            # Explore all neighbors of the current node
            for neighbor, weight in adj_map[node]:
                # Update the component cost by performing a bitwise AND of the edge weights
                component_cost &= weight

                # If the neighbor hasn't been visited, mark it as visited and add it to the queue
                if visited[neighbor]:
                    continue

                visited[neighbor] = True
                nodes_queue.append(neighbor)

        return component_cost

    # Use modified UnionFind but instead of storing rank just store the weight of the walk
    # Time O(V*N)
    # Space O(V+N)
    def minimumCost_union_find(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Create UnionFind and get weights
        uf = UnionFind(n)
        for source, dest, weight in edges:
            uf.union(source, dest, weight)

        answer = []
        for source, dest in query:
            answer.append(uf.get_cost(source, dest))

        return answer
    
test_cases = [
    [[0,0,0,0,0,0,0,0,0,0], 4, [[2,3,1],[1,3,5],[1,2,6],[3,0,7],[1,3,7],[0,2,5],[0,1,7]], [[2,1],[1,2],[0,1],[2,0],[0,2],[1,2],[3,2],[0,3],[2,1],[1,2]]],
    [[1,-1], 5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]]],
    [[0], 3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]]
]
solution = Solution()
for expected, n, edges, query in test_cases:
    actual = solution.minimumCost(n, edges, query)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}.")
        print(f"\tINPUTS: n: {n}, edges: {edges}, query: {query}")

print("Ran all tests")