from collections import defaultdict

# Preprocess all prime factors within problem range
MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)

class Solution:
    # Preprocess indices that can be jumped to then do BFS
    # Time O(n)
    # Space O(n)
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)

        # Create a list of edges for the prime numbers
        # Map is a num to any indexes it can go to
        edges = defaultdict(list[int])
        for i, num in enumerate(nums):
            for p in factors[num]:
                edges[p].append(i)

        jumps = 0

        # Create a list of what's been visited to make sure we don't cycle
        visited = [False] * n
        visited[0] = True
        # Not using deque because would then need to store in deque number of hops
        # Whereas with this we do all the hops at once by going through full queue
        q = [0]
        while True:
            q_next = []
            # Go over all things we can get to from this hop
            for i in q:
                # If we found the answer return number of jumps
                if i == n - 1:
                    return jumps
                # Go to neighbor right before if not yet visited
                if i > 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q_next.append(i - 1)
                # No to neighbor right after if not yet visited
                if i < n - 1 and not visited[i + 1]:
                    visited[i + 1] = True
                    q_next.append(i + 1)
                # See if number is prime and append all indices we can go to
                if len(factors[nums[i]]) == 1:
                    p = nums[i]
                    for j in edges[p]:
                        if not visited[j]:
                            visited[j] = True
                            q_next.append(j)

                    # Efficiency gain to just clear all these indices so we don't need to check again
                    edges[p].clear()

            q = q_next
            jumps += 1

test_cases = [
    [2, [1,2,4,6]],
    [2, [2,3,4,7,9]],
    [3, [4,6,5,8]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minJumps(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
