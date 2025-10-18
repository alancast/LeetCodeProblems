import math
from typing import List


class Solution:
    # Sort the array and greedily take any unique items
    # Time O(nlogn + n)
    # Space O(n) for sorting algo
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        answer = 0
        prev = -math.inf
        # Go over all nums and greedily take lowest possible
        for num in nums:
            # Find the lowest number not already used
            curr = min(max(num - k, prev + 1), num + k)

            # See if this number can be added as a new one
            if curr > prev:
                answer += 1
                prev = curr

        return answer

test_cases = [
    [6, [1,2,2,3,3,4], 2],
    [3, [4,4,4,4], 1]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.maxDistinctElements(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
