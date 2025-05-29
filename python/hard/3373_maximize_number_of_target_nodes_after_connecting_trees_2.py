from typing import List


class Solution:
    # DFS of two trees
    # The key finding is for a given u and v, if they are target each other
    # Then they have the same number of target nodes
    # So really we just need 2 counts, an even and an odd
    # Time O(n + m) as we compute for n (and m) nodes.
    # Space O(n + m) as colors1 is size n and colors2 is size m
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # 1 less edge than nodes
        n = len(edges1) + 1
        m = len(edges2) + 1

        colors1 = [0] * n
        colors2 = [0] * m

        # Compute counts (which is just even and odd)
        counts1 = self._compute_counts_for_even_and_odd_colors(edges1, colors1)
        counts2 = self._compute_counts_for_even_and_odd_colors(edges2, colors2)

        # Whether to connect with even or odd node in tree
        maxCounts2 = max(counts2[0], counts2[1])

        answer = [0] * n
        for i in range(n):
            # Answer is count from that node (even or odd) 
            # plus max of whether to connect with even or odd in second tree
            answer[i] = counts1[colors1[i]] + maxCounts2

        return answer
    
    # DFS on tree and add each node with a color 0 (for even depth) or 1 (for odd depth)
    # Time O(n) where n is len(children)
    # Space O(n)
    def _dfs(self, node: int, parent: int, depth: int, children: List[List[int]], colors: List[int]) -> int:
        # Only count even numbers
        count = 1 - depth % 2

        # Set the color for this node
        colors[node] = depth % 2

        # Get counts and colors from all it's children
        for child in children[node]:
            # No need to keep visited as each node just has two edges, one from parent, one to child
            # But make sure we don't go backward to parent
            if child == parent:
                continue

            count += self._dfs(child, node, depth + 1, children, colors)

        return count

    # Computes the amount of nodes reachable from an even or odd node
    # Time O(n + n) first n is for creating children, second n is for dfs
    # Space O(n)
    def _compute_counts_for_even_and_odd_colors(self, edges: List[List[int]], colors: List[int]) -> List[int]:
        # 1 less edge than nodes
        n = len(edges) + 1

        # Create children arrays for every node
        children = [[] for _ in range(n)]
        for u, v in edges:
            children[u].append(v)
            children[v].append(u)
        
        count_even = self._dfs(0, -1, 0, children, colors)

        # Count_even and count_odd must add up to n, so the math here is simple
        return [count_even, n - count_even]
    
test_cases = [
    [[8,7,7,8,8], [[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]],
    [[3,6,6,6,6], [[0,1],[0,2],[0,3],[0,4]], [[0,1],[1,2],[2,3]]]
]
solution = Solution()
for expected, edges1, edges2 in test_cases:
    actual = solution.maxTargetNodes(edges1, edges2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: edges1: {edges1}, edges2: {edges2}")

print("Ran all tests")