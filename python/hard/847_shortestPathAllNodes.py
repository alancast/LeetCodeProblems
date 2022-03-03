from typing import List


class Solution:
    # Breadth first search with bitmask
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        
        n = len(graph)
        # Bitmask being used. 0 for every node that we haven't been to yet. Turns to 1 when we visit it
        # So when all visited all n nodes will be 1
        ending_mask = (1 << n) - 1
        # Every possible starting node
        queue = [(node, 1 << node) for node in range(n)]
        # Used to not go back to the same node with the exact same set of nodes visited already
        seen = set(queue)

        steps = 0
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return 1 + steps
                    
                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))
            
            steps += 1
            queue = next_queue

testCases = [
    [[[1,2,3],[0],[0],[0]], 4],
    [[[1],[0,2,4],[1,3,4],[2],[1,2]], 4]
]
implementation = Solution()
for graph, expected in testCases:
    answer = implementation.shortestPathLength(graph)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. Graph: {graph}")