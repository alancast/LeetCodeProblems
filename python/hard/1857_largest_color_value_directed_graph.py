from collections import defaultdict, deque
from typing import List


class Solution:
    # Kahn's Algorithm with in degree and topological sort
    # Go through every node that has an edge going into it and remove all outgoing
    # Once every node is processed we have answer
    # If removing all outgoing nodes doesn't product any new nodes with in degree 0
    # Then either there is a cycle or we have processed all nodes
    # Time O(n+e) as we process all nodes and all edges
    # Space O(n+e) as we store adjacency graph of size e and in degree array of size n
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        # Create and populate adjacency graph and in_degree
        in_degree = [0] * n # number of edges going into node i
        adjacency_graph = defaultdict(list)
        for source, dest in edges:
            adjacency_graph[source].append(dest)
            in_degree[dest] += 1

        # Count array keeping track of max frequency for all colors for all paths ending at x
        count = [[0] * 26 for _ in range(n)]

        # Create a queue of all nodes with in_degree 0
        nodes_visited = 0
        q = deque()
        for i, num in enumerate(in_degree):
            if num == 0:
                q.append(i)

        # BFS to process all nodes
        answer = 0
        while q:
            node = q.popleft()
            nodes_visited += 1

            node_color = ord(colors[node]) - ord('a')
            count[node][node_color] += 1
            answer = max(answer, count[node][node_color])

            # Decrement in_degree for all neighbors and add to queue if zero
            for neighbor in adjacency_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                
                # Update color counts for all colors
                for i in range(26):
                    count[neighbor][i] = max(count[neighbor][i], count[node][i])

        # This means there was a cycle
        if nodes_visited < n:
            return -1

        return answer
    
test_cases = [
    [3, "abaca", [[0,1],[0,2],[2,3],[3,4]]],
    [-1, "a", [[0,0]]]
]
solution = Solution()
for expected, colors, edges in test_cases:
    actual = solution.largestPathValue(colors, edges)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: colors: {colors}, edges: {edges}")

print("Ran all tests")