from heapq import heappop, heappush


class Solution:
    INF = 9999999999999

    # Djikstras algorithm with a priority queue to find the minimum cost to reach city n-1 with discounts.
    # Time O((E + V) * log(V)) where E is the number of
    # Space O(V * D) where V is the number of cities and D is the number of discounts
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        # Construct the graph from the given highways array
        graph = [[] for _ in range(n)]
        for highway in highways:
            u, v, toll = highway
            graph[u].append((v, toll))
            graph[v].append((u, toll))

        # Min-heap priority queue to store tuples of (cost, city, discounts used)
        pq = [(0, 0, 0)]  # Start from city 0 with cost 0 and 0 discounts used

        # 2D array to track minimum distance to each city with a given number of discounts used
        dist = [[self.INF] * (discounts + 1) for _ in range(n)]
        dist[0][0] = 0

        while pq:
            current_cost, city, discounts_used = heappop(pq)

            # If this cost is already higher than the known minimum, skip it
            if current_cost > dist[city][discounts_used]:
                continue

            # Explore all neighbors of the current city
            for neighbor, toll in graph[city]:
                # Case 1: Move to the neighbor without using a discount
                if current_cost + toll < dist[neighbor][discounts_used]:
                    dist[neighbor][discounts_used] = current_cost + toll
                    heappush(
                        pq,
                        (
                            dist[neighbor][discounts_used],
                            neighbor,
                            discounts_used,
                        ),
                    )

                # Case 2: Move to the neighbor using a discount if available
                if discounts_used < discounts:
                    new_cost_with_discount = current_cost + toll // 2
                    if (
                        new_cost_with_discount
                        < dist[neighbor][discounts_used + 1]
                    ):
                        dist[neighbor][
                            discounts_used + 1
                        ] = new_cost_with_discount
                        heappush(
                            pq,
                            (
                                new_cost_with_discount,
                                neighbor,
                                discounts_used + 1,
                            ),
                        )

        # Find the minimum cost to reach city n-1 with any number of discounts used
        min_cost = min(dist[n - 1])
        return -1 if min_cost == self.INF else min_cost

test_cases = [
    [9, 5, [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], 1],
    [8, 4, [[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]], 20],
    [-1, 4, [[0,1,3],[2,3,2]], 0]
]
solution = Solution()
for expected, n, highways, discounts in test_cases:
    actual = solution.minimumCost(n, highways, discounts)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, highways: {highways}, discounts: {discounts}")

print("Ran all tests")
