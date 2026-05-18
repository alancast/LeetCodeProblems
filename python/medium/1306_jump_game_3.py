from collections import deque


class Solution:
    # BFS solution, mark indexes as visited when visited
    # Time O(n)
    # Space O(m)
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)

        # Create the queue and do BFS
        q = deque([start])
        while q:
            node = q.popleft()

            # Check if we have end goal
            if arr[node] == 0:
                return True

            # Can only move for positive values
            if arr[node] < 0:
                continue

            # Add potential next values to queue
            for i in [node + arr[node], node - arr[node]]:
                if 0 <= i < n:
                    q.append(i)

            # Mark as visited without extra space
            arr[node] = -arr[node]

        # No more spaces we can get to, so we have failed
        return False

test_cases = [
    [True, [4,2,3,0,3,1,2], 5],
    [True, [4,2,3,0,3,1,2], 0],
    [False, [3,0,2,1,2], 2]
]
solution = Solution()
for expected, arr, start in test_cases:
    actual = solution.canReach(arr, start)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: arr: {arr}, start: {start}")

print("Ran all tests")
