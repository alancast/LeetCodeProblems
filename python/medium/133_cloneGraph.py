from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        # Dictionary where key is initial node and value is cloned node (to avoid cycles)
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, [])

        while q:
            nextNode = q.popleft()
            for neighbor in nextNode.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)

                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[nextNode].neighbors.append(visited[neighbor])

        return visited[node]