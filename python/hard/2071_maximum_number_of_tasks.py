from collections import deque
from sortedcontainers import SortedList
from typing import List


class Solution:
    # Solve with a function to see if it's possible to complete k tasks
    # Then find maximum value of k that works and that's the answer
    # Time O(nlogn + mlogm + min(m,n)logmin(m,n)) 
    # first two are for sorting lists, third is for check function
    # Space O(logn+logm+min(m,n)) (again first ones are for sort, then min is for the binary search)
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)
        tasks.sort()
        # Sort from strongest to weakest
        workers.sort(reverse=True)

        # Check to see if we can complete k tasks
        def can_complete_k_tasks(k: int) -> bool:
            workers_idx = 0
            p = pills
            q = deque()
            # Enumerate each task from largest to smallest to see if it can be solved
            for i in range(k - 1, -1, -1):
                # If the strongest worker can work the hardest task right away
                if not q and workers[workers_idx] >= tasks[i]:
                    workers_idx += 1
                    continue

                # Can a worker in the q waiting for work accomplish the task without a pill
                if q and q[0] >= tasks[i]:
                    q.popleft()
                    continue

                # Add more potential candidates to the q (who might need to use a pill)
                while workers_idx < k and workers[workers_idx] + strength >= tasks[i]:
                    q.append(workers[workers_idx])
                    workers_idx += 1

                # Needed to use a pill so have the weakest worker do it
                if q and p > 0:
                    q.pop()
                    p -= 1
                    continue

                # No workers to complete the task
                return False
            
            return True

        # Binary search to see largest k whose tasks we can complete
        left = 1
        right = min(m, n)
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if can_complete_k_tasks(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer

    # Solve with a function to see if it's possible to complete k tasks
    # Then find maximum value of k that works and that's the answer
    # Time O(nlogn+mlogm + min(m,n)log^2min(m,n)) (first ones are for sorting lists)
    # Space O(logn+logm+min(m,n)) (again first ones are for sort, then min is for the binary search)
    def maxTaskAssign_suboptimal_check_helper(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)
        tasks.sort()
        workers.sort()

        # Check to see if we can complete k tasks
        def can_complete_k_tasks(k: int) -> bool:
            p = pills
            # Ordered set of workers (with the k highest value)
            ws = SortedList(workers[m - k :])
            # Enumerate each task from largest to smallest
            for i in range(k - 1, -1, -1):
                # If the largest element in the ordered set is greater than or equal to tasks[i]
                # Use that worker. Can be greedy because if smaller worker would suffice
                # Then they will also suffice for all subsequent tasks
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    # No pills left so it can't be solved
                    if p == 0:
                        return False
                    
                    # Find the lowest index of the sorted list that can solve it with a pill
                    rep = ws.bisect_left(tasks[i] - strength)
                    # If it is the end of the list that means none existed, so can't be solved
                    if rep == len(ws):
                        return False
                    
                    # Use pill and pop that worker
                    p -= 1
                    ws.pop(rep)
            return True

        # Binary search to see largest k whose tasks we can complete
        left = 1
        right = min(m, n)
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if can_complete_k_tasks(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
    
test_cases = [
    [3, [3,2,1], [0,3,3], 1, 1],
    [1, [5,4], [0,0,0], 1, 5],
    [2, [10,15,30], [0,10,10,10,10], 3, 10],
    [3, [5,10,15], [2,5,10,12], 1, 3]
]
solution = Solution()
for expected, tasks, workers, pills, strength in test_cases:
    actual = solution.maxTaskAssign(tasks, workers, pills, strength)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: Tasks: {tasks}, workers: {workers}, pills: {pills}, strength: {strength}")

print("Ran all tests")