from collections import defaultdict


class Solution:
    UNPROCESSED = 0
    PROCESSING = 1
    PROCESSED = 2

    # Can't really do bfs because of cycles
    # Do DFS, each node has 3 states: UNPROCESSED, PROCESSING, PROCESSED
    # Once all nodes are processed they should all go to destination
    # If they don't then it fails
    # Time O(V + E)
    # Space O(V + E)
    def leadsToDestination(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # Create graph of edges. Map of source to all destinations
        graph = self.build_graph(n, edges)

        # See if all paths lead to the same destination
        return self.leads_to_dest(graph, source, destination, [Solution.UNPROCESSED] * n)

    def build_graph(self, n: int, edges: list[list[int]]) -> defaultdict:
        graph = defaultdict(list[int])

        for source, dest in edges:
            graph[source].append(dest)

        return graph

    def leads_to_dest(self, graph: defaultdict, node: int, dest: int, states: list[int]) -> bool:
        # If any processing has started on this node
        # If it's not fully processed that means it is part of a cycle (which means it fails)
        if states[node] != Solution.UNPROCESSED:
            return states[node] == Solution.PROCESSED

        # If this is a leaf node, it should be equal to the destination.
        if node not in graph:
            return node == dest

        # Now, we are processing this node. So we mark it as such.
        states[node] = Solution.PROCESSING

        for next_node in graph[node]:
            # If we get a `false` from any recursive call on the neighbors
            # We short circuit and return from there
            if not self.leads_to_dest(graph, next_node, dest, states):
                return False

        # Recursive processing done for the node. We mark it PROCESSED.
        states[node] = Solution.PROCESSED
        return True

test_cases = [
    [False, 3, [[0,1],[0,2]], 0, 2],
    [False, 4, [[0,1],[0,3],[1,2],[2,1]], 0, 3],
    [True, 4, [[0,1],[0,3],[1,2],[2,1]], 0, 3]
]
solution = Solution()
for expected, n, edges, source, destination in test_cases:
    actual = solution.leadsToDestination(n, edges, source, destination)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, edges: {edges}, source: {source}, destination: {destination}")

print("Ran all tests")
