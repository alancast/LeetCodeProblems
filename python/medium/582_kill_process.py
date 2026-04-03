from collections import defaultdict, deque


class Solution:
    # Create a mapping of parent to children
    # Then just use a queue to return all children tasks
    # Time O(n)
    # Space O(n)
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        # Create parent to children mapping
        children = defaultdict(list[int])
        for i, parent in enumerate(ppid):
            children[parent].append(pid[i])

        answer = []
        # Fetch all children of the process that's being killed
        queue = deque([kill])
        while queue:
            id = queue.popleft()
            answer.append(id)

            queue.extend(children[id])

        return answer

test_cases = [
    [[5,10], [1,3,10,5], [3,0,5,3], 5],
    [[1], [1], [0], 1]
]
solution = Solution()
for expected, pid, ppid, kill in test_cases:
    actual = solution.killProcess(pid, ppid, kill)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: pid: {pid}, ppid: {ppid}, kill: {kill}")

print("Ran all tests")
