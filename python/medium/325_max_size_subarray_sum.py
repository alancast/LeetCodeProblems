from collections import defaultdict
from typing import List


class Solution:
    # Time O(n) as we go over nums once
    # Space O(n) as map could be entirely different sums
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Map of prefix sum to the first index where it happens
        p_sum_to_first_index_map = defaultdict(int)
        p_sum_to_first_index_map[0] = -1

        # Create prefix sum index mapping
        max_distance = 0
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            target_sum = prefix_sum - k

            # See if number we are looking for is already there and is longer array
            if target_sum in p_sum_to_first_index_map and \
                (i - p_sum_to_first_index_map[target_sum]) > max_distance:
                max_distance = i - p_sum_to_first_index_map[target_sum]

            # Add this prefix sum to the map
            if prefix_sum not in p_sum_to_first_index_map:
                p_sum_to_first_index_map[prefix_sum] = i

        return max_distance
    
test_cases = [
    [4, [1,-1,5,-2,3], 3],
    [2, [-2,-1,2,1], 1],
    [0, [1], 0]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.maxSubArrayLen(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}, k: {k}")

print("Ran all tests")