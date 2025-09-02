from heapq import heappop, heappush
from typing import List


class Solution:
    # Basically djikstras with bitmasking as we are guaranteed less than 10 bikes
    # So mask with 10 bit num and compute total cost each time
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        # Compute the manhattan distance from a worker to a bike
        def manhattan_dist(worker_index: int, bike_index: int) -> int:
            x_dist = abs(workers[worker_index][0] - bikes[bike_index][0])
            y_dist = abs(workers[worker_index][1] - bikes[bike_index][1])
            return x_dist + y_dist

        # Min cost heap for djikstras 
        # Stores total cost (sort key), worker_index matched, which bikes are taken
        min_cost_heap = [[0, 0, 0]]
        # What worker index, bikes taken combinations we've already computed
        seen = set()

        # Go until we have placed all the workers
        while True:
            cost, worker_index, bikes_taken = heappop(min_cost_heap)

            # If we've already seen this combo with a lower value continue
            if (worker_index, bikes_taken) in seen:
                continue

            # Add this combination to what we've seen
            seen.add((worker_index, bikes_taken))

            # We've matched all the workers with a bike and thus this is the min cost
            if worker_index == len(workers):
                return cost

            # Go over all free bikes and push the new manhattan distance if this worker takes them
            for bike_index in range(len(bikes)):
                # Bike isn't taken so add the possibility of taking this bike to the djikstras queue
                if bikes_taken & (1 << bike_index) == 0:
                    heappush(
                        min_cost_heap,
                        [
                            cost + manhattan_dist(worker_index, bike_index),
                            worker_index + 1,
                            bikes_taken | (1 << bike_index)
                        ]
                    )

test_cases = [
    [6, [[0,0],[2,1]], [[1,2],[3,3]]],
    [4, [[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]],
    [4995, [[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]]]
]
solution = Solution()
for expected, workers, bikes in test_cases:
    actual = solution.assignBikes(workers, bikes)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: workers: {workers}, bikes: {bikes}")

print("Ran all tests")