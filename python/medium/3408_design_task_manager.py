from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class TaskManager:
    # Priority queue of (TaskPri, TaskId, UserId) sorted by first 2
    task_pq: List
    # Map task to priority
    task_to_priority: defaultdict
    # Map task to user (for edit to work properly)
    task_to_user: defaultdict

    # Time O(nlogn)
    def __init__(self, tasks: List[List[int]]):
        self.task_pq = []
        self.task_to_priority = defaultdict(int)
        self.task_to_user = defaultdict(int)

        # Initialize structures
        for user_id, task_id, priority in tasks:
            self.task_to_priority[task_id] = priority
            self.task_to_user[task_id] = user_id
            heappush(self.task_pq, (-priority, -task_id, user_id))
        

    # Time O(logn)
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_priority[taskId] = priority
        self.task_to_user[taskId] = userId
        heappush(self.task_pq, (-priority, -taskId, userId))

    # Time O(logn)
    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_to_priority[taskId] = newPriority
        heappush(self.task_pq, (-newPriority, -taskId, self.task_to_user[taskId]))

    # Time O(1)
    def rmv(self, taskId: int) -> None:
        del self.task_to_priority[taskId]
        del self.task_to_user[taskId]   

    # Time O(n worst case)
    def execTop(self) -> int:
        while self.task_pq:
            priority, task_id, user_id = heappop(self.task_pq)

            # Make sure the task in the pq is up to date and belongs to right user
            if (
                -task_id not in self.task_to_priority
                or -priority != self.task_to_priority[-task_id]
                or user_id != self.task_to_user[-task_id]
            ):
                continue

            # Remove the processed task from the maps and return the userId
            del self.task_to_priority[-task_id]
            del self.task_to_user[-task_id]

            return user_id

        # No valid tasks left, so return -1
        return -1



# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
