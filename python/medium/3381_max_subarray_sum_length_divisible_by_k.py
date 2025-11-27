from sys import maxsize
from typing import List


class Solution:
    # Compute prefix sum and use that to find sum of range
    # Keep an array of min sum for a mod k range
    # Time O(n)
    # Space O(k)
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix_sum = 0
        answer = -maxsize

        # Min sum of length mod k
        min_mod_k_sum = [maxsize // 2] * k
        min_mod_k_sum[k - 1] = 0

        # Go over all nums and update sums
        for i in range(n):
            prefix_sum += nums[i]
            # max of current max or prefix sum - smallest prefix sum of a length mod k
            answer = max(answer, prefix_sum - min_mod_k_sum[i % k])
            # See if this sum is smaller than the one currently stored in the mod k
            min_mod_k_sum[i % k] = min(min_mod_k_sum[i % k], prefix_sum)

        return answer

test_cases = [
    [3, [1,2], 1],
    [-10, [-1,-2,-3,-4,-5], 4],
    [4, [-5,1,2,-3,4], 2]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.maxSubarraySum(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")