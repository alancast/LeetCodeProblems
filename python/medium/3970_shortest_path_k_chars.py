from heapq import heappop, heappush


class Solution:
    # Use Dijkstra's algorithm with the current matching-label streak as part of each state.
    # Time O(E * k * log(E * k))
    # Space O(E * k + V * k)
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # Build the directed graph from the given edges.
        graph = [[] for _ in range(n)]
        for start, end, weight in edges:
            graph[start].append((end, weight))

        # Track the shortest distance to each node with each possible streak length.
        distances = [[2**31 - 1] * (k + 1) for _ in range(n)]

        # Store (distance, node, matching-label streak) in the min-heap.
        priority_queue = [(0, 0, 1)]
        distances[0][1] = 0

        # Explore paths in order of increasing distance.
        while priority_queue:
            distance, node, streak = heappop(priority_queue)

            # Skip states that were already reached with a shorter path.
            if distance > distances[node][streak]:
                continue
            if node == n - 1:
                return distance

            # Extend the streak if the next node has the same label.
            for neighbor, weight in graph[node]:
                new_streak = streak + 1 if labels[node] == labels[neighbor] else 1
                if new_streak > k:
                    continue

                new_distance = distance + weight
                if new_distance < distances[neighbor][new_streak]:
                    distances[neighbor][new_streak] = new_distance
                    heappush(
                        priority_queue, (new_distance, neighbor, new_streak)
                    )

        return -1

test_cases = [
    [3, 3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1],
    [2, 3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2],
    [-1, 3, [[0, 1, 1], [1, 2, 1]], "aaa", 2],
]
solution = Solution()
for expected, n, edges, labels, k in test_cases:
    actual = solution.shortestPath(n, edges, labels, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, edges: {edges}, labels: {labels}, k: {k}")

print("Ran all tests")
