from collections import Counter
from heapq import heapify, heappop, heappush
from math import sqrt
from typing import List


class Solution:
    # Build up num of cars until they are all processed
    # Time O(n + mlogk) where m is num cars, k is max rank
    # O(n) for counter O(k) for building heap 
    # O(logk) for each heap operation inside loop which could run m times
    # Space O(k) as we have heap of size k
    def repairCars(self, rank: List[int], cars: int) -> int:
        # Count the frequency of each rank
        count = Counter(rank)

        # Create a Min-heap storing [time, rank, n, count]:
        # Sorted by time
        # - time: time for the next repair
        # - rank: mechanic's rank
        # - n: cars repaired by this mechanic
        # - count: number of mechanics with this rank
        # Initial time = rank (as rank * 1^2 = rank)
        min_heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(min_heap)

        # Process until all cars are repaired
        while cars > 0:
            # Pop the mechanic with the smallest current repair time
            time, rank, n, count = heappop(min_heap)

            # Deduct the number of cars repaired by this mechanic group
            cars -= count

            # Increment the number of cars repaired by this mechanic
            n += 1

            # Push the updated repair time back into the heap
            # The new repair time is rank * n^2 (since time increases quadratically with n)
            heappush(min_heap, [rank * n * n, rank, n, count])

        return time

    # Binary search to see if given minute could work
    # Could be optimized by creating frequency array and breaking out of loop early
    # Time O(nlogn)
    # Space O(1)
    def repair_cars_binary_search(self, ranks: List[int], cars: int) -> int:
        best_mechanic = min(ranks)
        left = 0
        right = best_mechanic * cars * cars

        answer = right
        while left <= right:
            # Same as (left + right) // 2 but avoids overflow
            mid = left + (right - left) // 2

            # See if it's possible to solve in this amount of minutes
            cars_fixed = 0
            for num in ranks:
                cars_fixed += int(sqrt((mid // num)))

            if cars_fixed >= cars:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
    
test_cases = [
    [16, [4,2,3,1], 10],
    [16, [5,1,8], 6]
]
solution = Solution()
for expected, ranks, cars in test_cases:
    actual = solution.repairCars(ranks, cars)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: ranks: {ranks}, cars: {cars}")

print("Ran all tests")