from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        destination = len(graph) - 1
        paths = []
        q = [[0]]
        while q:
            current_path = q.pop()
            neighbors = graph[current_path[-1]]
            for node in neighbors:
                if node == destination:
                    successful_path = current_path.copy()
                    successful_path.append(destination)
                    paths.append(successful_path)
                    continue
                next_path = current_path.copy()
                next_path.append(node)
                q.append(next_path)

        return paths