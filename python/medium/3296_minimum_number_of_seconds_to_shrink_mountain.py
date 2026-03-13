from heapq import heappop, heappush


class Solution:
    # Binary search of times and see which one works
    # Time O(nlogn) where n is len worker times
    # Space O(1)
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        left = 1
        right = self._compute_time(max(workerTimes), mountainHeight)
        answer = 0

        error = 1e-7
        # Do the binary search
        while left <= right:
            mid = (left + right) // 2
            work_done = 0
            for time in workerTimes:
                work = mid // time

                # Find the largest k such that 1+2+...+k <= work
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2 + error)
                work_done += k

            # Update bounds if we did or did not clear mountain in this time
            if work_done >= mountainHeight:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer


    # Create a priority queue of times, and just keep popping them until height is zero
    # Time O(nlogn) where n is len worker times
    # Space O(n)
    def minNumberOfSeconds_simulation(self, mountainHeight: int, workerTimes: list[int]) -> int:
        # Create initial worker times
        pq = []
        for time in workerTimes:
            heappush(pq, (time, time, 1))

        answer = 0
        # Keep popping off the queue until the mountain is 0
        while mountainHeight > 0:
            answer, time, seconds = heappop(pq)
            mountainHeight -= 1

            # Re add to queue how much it would take for next bit of work added
            heappush(pq, (self._compute_time(time, seconds + 1), time, seconds + 1))

        return answer

    # Returns the amount of time for a worker to work for that many seconds
    # Time O(1)
    # Space O(1)
    def _compute_time(self, time: int, seconds: int) -> int:
        # Formula is (seconds * (seconds + 1)) // 2 * time
        return ((seconds * (seconds + 1)) // 2) * time

test_cases = [
    [3, 4, [2,1,1]],
    [12, 10, [3,2,2,4]],
    [15, 5, [1]]
]
solution = Solution()
for expected, mountain_height, worker_times in test_cases:
    actual = solution.minNumberOfSeconds(mountain_height, worker_times)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: mountain_height: {mountain_height}, worker_times: {worker_times}")

print("Ran all tests")
