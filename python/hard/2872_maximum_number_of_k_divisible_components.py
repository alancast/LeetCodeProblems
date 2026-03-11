from collections import defaultdict, deque


class Solution:
    # BFS
    # Check each leaf node. If it is divisible by k then make it it's own component
    # If it isn't, combine it with parent
    # Repeat that process until all nodes are done
    # Time O(n)
    # Space O(n)
    def maxKDivisibleComponents(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:
        # Base case: if there are less than 2 nodes, return 1
        if n < 2:  # noqa: PLR2004
            return 1

        component_count = 0
        graph = defaultdict(set)

        # Step 1: Build the graph
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        # Step 2: Initialize the BFS queue with leaf nodes (nodes with only one connection)
        queue = deque(
            node for node, neighbors in graph.items() if len(neighbors) == 1
        )

        # Step 3: Process nodes in BFS order
        while queue:
            current_node = queue.popleft()
            neighbor_node = (
                next(iter(graph[current_node])) if graph[current_node] else -1
            )

            # Remove the edge between current and neighbor
            if neighbor_node >= 0:
                graph[neighbor_node].remove(current_node)

            # Check divisibility of the current node's value
            if values[current_node] % k == 0:
                component_count += 1
            else:
                values[neighbor_node] += values[current_node]

            # If the neighbor becomes a leaf node, add it to the queue
            if neighbor_node >= 0 and len(graph[neighbor_node]) == 1:
                queue.append(neighbor_node)

        return component_count

    # DFS
    # Check subtree sums. If any subtree sum mod k == 0 make it a new component
    # Repeat that process until all nodes are done
    # Time O(n)
    # Space O(n)
    def maxKDivisibleComponents_dfs(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        # Step 1: Create adjacency list from edges
        adj_list = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        # Step 2: Initialize component count
        component_count = [0]  # Use a list to pass by reference

        # Step 3: Start DFS traversal from node 0
        self._dfs(0, -1, adj_list, values, k, component_count)

        # Step 4: Return the total number of components
        return component_count[0]

    def _dfs(  # noqa: PLR0913
        self,
        current_node: int,
        parent_node: int,
        adj_list: list[list[int]],
        node_values: list[int],
        k: int,
        component_count: list[int],
    ) -> int:
        # Step 1: Initialize sum for the current subtree
        subtree_sum = 0

        # Step 2: Traverse all neighbors
        for neighbor_node in adj_list[current_node]:
            if neighbor_node != parent_node:
                # Recursive call to process the subtree rooted at the neighbor
                subtree_sum += self._dfs(
                    neighbor_node,
                    current_node,
                    adj_list,
                    node_values,
                    k,
                    component_count,
                )
                subtree_sum %= k  # Ensure the sum stays within bounds

        # Step 3: Add the value of the current node to the sum
        subtree_sum += node_values[current_node]
        subtree_sum %= k

        # Step 4: Check if the sum is divisible by k
        if subtree_sum == 0:
            component_count[0] += 1

        # Step 5: Return the computed sum for the current subtree
        return subtree_sum

test_cases = [
    [2, 5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6],
    [3, 7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3]
]
solution = Solution()
for expected, n, edges, values, k in test_cases:
    actual = solution.maxKDivisibleComponents(n, edges, values, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, edges: {edges}, values: {values}, k: {k}")

print("Ran all tests")
