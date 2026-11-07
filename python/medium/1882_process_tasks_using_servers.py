from heapq import heapify, heappop, heappush


class Solution:
    # Priority queue solution
    # Time O((n + m) * log(n)) where n is the number of servers and m is the number of tasks
    # Space O(n)
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Busy servers, stored as pairs (t, idx)
        busy = []

        # Idle servers, stored as pairs (w, idx)
        idle = [(w, i) for i, w in enumerate(servers)]
        heapify(idle)

        ts = 0

        # Move servers with t<=ts from priority queue busy to priority queue idle one by one
        def release():
            while busy and busy[0][0] <= ts:
                _, idx = heappop(busy)
                heappush(idle, (servers[idx], idx))

        answer = []
        for i, task in enumerate(tasks):
            ts = max(ts, i)
            release()
            if not idle:
                ts = busy[0][0]
                release()

            _, idx = heappop(idle)
            answer.append(idx)
            heappush(busy, (ts + task, idx))

        return answer

test_cases = [
    [[2, 2, 0, 2, 1, 2], [3, 3, 2], [1, 2, 3, 2, 1, 2]],
    [[1, 4, 1, 4, 1, 3, 2], [5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]],
]
solution = Solution()
for expected, servers, tasks in test_cases:
    actual = solution.assignTasks(servers, tasks)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: servers: {servers}, tasks: {tasks}")

print("Ran all tests")

