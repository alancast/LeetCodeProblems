from typing import List


class Solution:
    # DFS of two trees to see how many nodes are reachable for a given k
    # Time O(nk + mk) as we compute for n (and m) nodes. And each computation is k steps
    # Space O(n+m) as counts1 is size n and counts2 is size m
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # 1 less edge than nodes
        n = len(edges1) + 1

        # Compute counts arrays
        counts1 = self._compute_counts_reachable_in_k_per_node(edges1, k)
        counts2 = self._compute_counts_reachable_in_k_per_node(edges2, k - 1)
        maxCounts2 = max(counts2)

        answer = []
        for i in range(n):
            answer.append(counts1[i] + maxCounts2)

        return answer
    
    # DFS to see how many nodes are reachable in k hops from a give node
    # Time O(k)
    # Space O(k)
    def _dfs(self, node: int, parent: int, children: List[List[int]], k: int) -> int:
        if k < 0:
            return 0
        
        # Can always reach itself
        count = 1

        # Get counts from all it's children
        for child in children[node]:
            # No need to keep visited as each node just has two edges, one from parent, one to child
            # But make sure we don't go backward to parent
            if child == parent:
                continue

            count += self._dfs(child, node, children, k - 1)

        return count

    # Computes the amount of nodes reachable from every node in k hops
    # Time O(nk) as we compute for n nodes. And each computation is k steps
    # Space O(n)
    def _compute_counts_reachable_in_k_per_node(self, edges: List[List[int]], k: int) -> List[int]:
        # 1 less edge than nodes
        n = len(edges) + 1

        # Create children arrays for every node
        children = [[] for _ in range(n)]
        for u, v in edges:
            children[u].append(v)
            children[v].append(u)
        
        # Create counts array
        counts = [0] * n

        # DFS on every node in tree
        for i in range(n):
            counts[i] = self._dfs(i, -1, children, k)
    
        return counts
    
test_cases = [
    [[9,7,9,8,8], [[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 2],
    [[6,3,3,3,3], [[0,1],[0,2],[0,3],[0,4]], [[0,1],[1,2],[2,3]], 1]
]
solution = Solution()
for expected, edges1, edges2, k in test_cases:
    actual = solution.maxTargetNodes(edges1, edges2, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: edges1: {edges1}, edges2: {edges2}, k: {k}")

print("Ran all tests")