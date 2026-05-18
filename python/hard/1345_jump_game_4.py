from collections import defaultdict, deque


class Solution:
    # Bidirectional BSF (faster)
    # Time O(n)
    # Space O(n)
    def minJumps(self, arr) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        # Go over all nums and map to all other indexes with same value
        graph = defaultdict(list[int])
        for i, num in enumerate(arr):
            graph[num].append(i)

        # Store items to search from beginning and end
        side_a = {0}
        side_b = {n-1}

        # Mark first and last as visited
        visited = {0, n-1}
        step = 0

        # As long as there are still things to visit
        while side_a:
            # Check whichever side has fewer nodes
            if len(side_a) > len(side_b):
                side_a, side_b = side_b, side_a
            next = set()

            # Iterate through all nodes in layer
            for node in side_a:

                # Check all with same value
                for child in graph[arr[node]]:
                    # If we have gotten there from other direction return final
                    if child in side_b:
                        return step + 1
                    # Mark as visited and add node
                    if child not in visited:
                        visited.add(child)
                        next.add(child)

                # Clear the list to prevent redundant search
                graph[arr[node]].clear()

                # Check neighbors before and after
                for child in [node-1, node+1]:
                    if child in side_b:
                        return step + 1
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        next.add(child)

            side_a = next
            step += 1

        # This would never happen (could throw here instead)
        return -1

    # Exceeds memory limit
    # BFS (first go over and add indices of all nums that are same)
    # Time O(n)
    # Space O(n) for queue and visited
    def minJumps_simple_bsf(self, arr: list[int]) -> int:
        n = len(arr)
        visited = [False] * n

        # Go over all nums and map to all other indexes with same value
        indexes_same_values = defaultdict(list[int])
        for i, num in enumerate(arr):
            indexes_same_values[num].append(i)

        # Create the queue and do BFS
        # Q stores: (num jumps, idx)
        q = deque([(0,0)])
        while q:
            num_jumps, node_idx = q.popleft()

            # Make sure we haven't already visited this node
            if visited[node_idx]:
                continue

            # Mark as visited
            visited[node_idx] = True

            # Check if we have end goal
            if node_idx == n-1:
                return num_jumps

            # Add before and behind
            if node_idx + 1 < n and not visited[node_idx + 1]:
                q.append((num_jumps + 1, node_idx + 1))
            if node_idx - 1 > 0 and not visited[node_idx - 1]:
                q.append((num_jumps + 1, node_idx - 1))

            # Add all idx with same value
            for idx in indexes_same_values[arr[node_idx]]:
                if not visited[idx]:
                    q.append((num_jumps + 1, idx))

        # We couldn't get to end. This is impossible, should throw
        return -1

test_cases = [
    [3, [100,-23,-23,404,100,23,23,23,3,404]],
    [0, [7]],
    [1, [7,6,9,6,9,6,9,7]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minJumps(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
