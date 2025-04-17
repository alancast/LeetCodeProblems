from collections import defaultdict
from typing import List


class Solution:
    # Basically a hand made UnionFind implementation.
    # Could have also implemented a UnionFind class
    # A completed connected component of n nodes has n(n-1)//2 edges
    # Create sets for each node, each time there is an edge union the component sets
    # At the end every component set with n(n-1)//2 edges in it is good
    # Time O(n + m^2) where m is length of edges as every edge could trigger into a component merge
    # Space O(n) where n is number of nodes (really 3n but simplifies to n)
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Map for what component each node is in
        node_component_map = defaultdict(int)
        # Mapping of component to what nodes are in it
        component_node_map = defaultdict(List[int])
        # Mapping of components to num edges in it
        component_edges = defaultdict(int)

        # Initialize data structures
        for i in range(n):
            component_edges[i] = 0
            node_component_map[i] = i
            component_node_map[i] = [i]

        # Go through each edge and union components from it
        for edge in edges:
            node_a = edge[0]
            node_b = edge[1]
            component_a = node_component_map[node_a]
            component_b = node_component_map[node_b]

            # They are already in the same component so add the edge and carry on
            if component_a == component_b:
                component_edges[component_a] += 1
                continue

            # They are in different components so merge them (merge comp b into comp a)
            # update all the nodes to map to the new component
            for node in component_node_map[component_b]:
                node_component_map[node] = component_a
                component_node_map[component_a].append(node)
            
            # Update edge count to have all the component b edges as well as the new one
            component_edges[component_a] += component_edges[component_b] + 1

            # Purge non-existing component b as it's now merged into a
            del component_node_map[component_b]
            del component_edges[component_b]


        # See how many of the components are complete
        complete_components = 0
        for component, num_edges in component_edges.items():
            num_nodes = len(component_node_map[component])
            if num_edges == ((num_nodes*(num_nodes-1))//2):
                complete_components += 1

        return complete_components
    
test_cases = [
    [3, 3, []],
    [2, 3, [[0,1]]],
    [1, 6, [[0,1],[0,2],[1,2],[3,4],[3,5]]],
    [0, 6, [[0,1],[0,2],[3,4],[3,5]]],
    [3, 6, [[0,1],[0,2],[1,2],[3,4]]]
]
solution = Solution()
for expected, n, edges in test_cases:
    actual = solution.countCompleteComponents(n, edges)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}, edges: {edges}")

print("Ran all tests")