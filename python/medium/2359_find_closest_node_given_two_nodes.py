from typing import List


class Solution:
    # Bidirectional DFS
    # Time O(n)
    # Space O(n)
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        visited1 = set()
        visited2 = set()

        # As long as one node is still searching, carry forward
        while node1 != -1 or node2 != -1:
            # Check for cycles in node1 and node2
            if node1 in visited1:
                node1 = -1
            if node2 in visited2:
                node2 = -1

            # First time seeing a node add it to the visited
            if node1 != -1:
                visited1.add(node1)
            if node2 != -1:
                visited2.add(node2)

            # We've already visited this node from both sides so we have answer
            if node1 in visited2 and node2 in visited1:
                return min(node1, node2)
            if node1 in visited2:
                return node1
            if node2 in visited1:
                return node2
            
            # Update node for next round
            if node1 != -1:
                node1 = edges[node1]
            if node2 != -1:
                node2 = edges[node2]       

        # In case there is no common node
        return -1

    # Do DFS from two nodes and sum distances, then find min of maxes
    # Time O(n)
    # Space O(n)
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        # Store distances to a node from node 1 and 2
        dist1 = [-1] * n
        self._dfs(node1, edges, dist1)
        dist2 = [-1] * n
        self._dfs(node2, edges, dist2)

        answer = -1
        min_of_max = float('inf')
        # Iterate over nodes to find the min of max
        for i in range(n):
            if dist1[i] >= 0 and dist2[i] >= 0:
                if max(dist1[i], dist2[i]) < min_of_max:
                    min_of_max = max(dist1[i], dist2[i])
                    answer = i

        return answer
    
    # Modifies distances array
    # Time O(n)
    def _dfs(self, current: int, edges: List[int], distances: list[int]) -> None:
        distance = 0

        # Search until we run out of edges or we hit a cycle
        while current != -1 and distances[current] == -1:
            distances[current] = distance
            distance += 1
            current = edges[current]
    
test_cases = [
    [4, [4,3,0,5,3,-1], 4, 0],
    [2, [2,2,3,-1], 0, 1],
    [2, [1,2,-1], 0, 2]
]
solution = Solution()
for expected, edges, node1, node2 in test_cases:
    actual = solution.closestMeetingNode(edges, node1, node2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: edges: {edges}, node1: {node1}, node2: {node2}")

print("Ran all tests")