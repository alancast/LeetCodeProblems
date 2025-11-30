from collections import defaultdict
from typing import List


class Solution:
    # Go over array and find prefix sum mod p
    # Time O(n)
    # Space O(n)
    def minSubarray(self, nums: List[int], p: int) -> int:
        num_sum = sum(nums)
        remainder = num_sum % p

        if remainder == 0:
            return 0

        prefix_sum_remainder = 0
        answer = len(nums)
        # Mapping of prefix sum mod p to rightmost index when it was seen
        seen = {0: -1}

        # Go over whole array and compute prefix sums and all that
        for i, num in enumerate(nums):
            prefix_sum_remainder = (prefix_sum_remainder + num) % p
            target = (prefix_sum_remainder - remainder) % p

            # See if something with this mod has already been seen
            if target in seen:
                answer = min(answer, i - seen[target])

            # Update prefix sum remainder
            seen[prefix_sum_remainder] = i

        # If it's never possible return -1
        return answer if answer < len(nums) else -1

test_cases = [
    [1, [3,1,4,2], 6],
    [2, [6,3,5,2], 9],
    [0, [1,2,3], 3]
]
solution = Solution()
for expected, nums, p in test_cases:
    actual = solution.minSubarray(nums, p)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, p: {p}")

print("Ran all tests")