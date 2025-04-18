from collections import deque
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        max_income = float("-inf")
        # Adjacency matrix
        tree = [[] for _ in range(n)]
        bob_path = dict()
        visited = [False] * n

        # Form adjacency matrix
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        # Inline DFS to find Bob's path
        # What this problem did a TERRIBLE job explaining is there is only 1 path
        # from any node a to node b. So there is only one path to node 0
        # So DFS works
        def find_bob_path(node, time):
            bob_path[node] = time
            visited[node] = True

            if node == 0:
                return True
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    if find_bob_path(neighbor, time + 1):
                        return True
            
            # If we reach here it means this node was not on Bob's path to 0
            bob_path.pop(node, None)
            return False

        # Find the path taken by Bob
        find_bob_path(bob, 0)

        # Breadth-First Search (BFS)
        visited = [False] * n
        queue = deque([(0, 0, 0)])

        while queue:
            node, time, income = queue.popleft()

            # Alice reaches the node first
            if node not in bob_path or time < bob_path[node]:
                income += amount[node]
            elif time == bob_path[node]:  # Alice and Bob arrive together
                income += amount[node] // 2

            # Update max value if current node is a leaf
            if len(tree[node]) == 1 and node != 0:
                max_income = max(max_income, income)

            # Explore adjacent unvisited nodes
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    queue.append((neighbor, time + 1, income))
            visited[node] = True

        return max_income
    
test_cases = [
    [6, [[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]],
    [-7280, [[0,1]], 1, [-7280,2350]]
]
solution = Solution()
for expected, edges, bob, amount in test_cases:
    actual = solution.mostProfitablePath(edges, bob, amount)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: edges: {edges}, bob: {bob}, amount: {amount}")

print("Ran all tests")