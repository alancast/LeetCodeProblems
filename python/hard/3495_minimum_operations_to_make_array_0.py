from typing import List


class Solution:
    # Go through each query and find out how many operations for that query
    # Time O(nlog(r))
    # Space O(1)
    def minOperations(self, queries: List[List[int]]) -> int:
        answer = 0

        # Go through each query and find out how many operations for that query
        for l, r in queries:
            query_sum = self._depth_sum(r) - self._depth_sum(l-1) + 1
            # Divide by 2 because we do two numbers at a time per operation
            answer += query_sum // 2

        return answer

    # Total 4 depth of all numbers from 1 to n
    # 4 depth is how many times divided by 4 for a number to become 0
    # So total 4depth is the sum of the 4depth of all numbers
    def _depth_sum(self, n: int) -> int:
        if n <= 0:
            return 0

        depth_sum = 0
        base = depth = 1
        while base <= n:
            # How many numbers in this power of 4 range
            count = min(n, base * 4 - 1) - base + 1
            # Depth sum is number of numbers in range time depth per number
            depth_sum += count * depth
            base *= 4
            depth += 1

        return depth_sum

test_cases = [
    [3, [[1,2],[2,4]]],
    [4, [[2,6]]]
]
solution = Solution()
for expected, queries in test_cases:
    actual = solution.minOperations(queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: queries: {queries}")

print("Ran all tests")