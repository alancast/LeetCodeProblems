from collections import deque


class Solution:
    # Search graph and see what methods can be removed
    # Time O(n+e)
    # Space O(n+e)
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # List for what each edge goes to as well as count of how many incoming per edge
        edges = [[] for _ in range(n)]
        in_degree = [0] * n

        # Populate edges and in degree count
        for u, v in invocations:
            edges[u].append(v)
            in_degree[v] += 1

        # Process suspicious functions until there are none left
        queue = deque([k])
        suspicious = bytearray(n)
        suspicious[k] = 1
        while queue:
            # Take front of queue
            u = queue.popleft()

            # Remove edge for all suspicious things
            for v in edges[u]:
                in_degree[v] -= 1

                # Add all newly suspicious things
                if suspicious[v] == 0:
                    queue.append(v)
                    suspicious[v] = 1

        # See if you can remove all the suspicious functions
        can_remove_all = True
        for i in range(n):
            # A function is suspicious and something is still calling into it so it can't be removed
            if suspicious[i] == 1 and in_degree[i] > 0:
                can_remove_all = False
                break

        # If you can't remove all the suspicious ones, then you can't remove any, so return all functions
        if not can_remove_all:
            return list(range(n))

        # Return all the functions that aren't suspicious
        return [i for i in range(n) if suspicious[i] == 0]

test_cases = [
    [[0,1,2,3], 4, 1, [[1,2],[0,1],[3,2]]],
    [[3,4], 5, 0, [[1,2],[0,2],[0,1],[3,4]]],
    [[], 3, 2, [[1,2],[0,1],[2,0]]]
]
solution = Solution()
for expected, n, k, invocations in test_cases:
    actual = solution.remainingMethods(n, k, invocations)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, k: {k}, invocations: {invocations}")

print("Ran all tests")
