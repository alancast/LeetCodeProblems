from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        return self._count_interesting_subarrays_prefix_sum(nums, modulo, k)

    # Doing some janky math gives us an equation where we can use prefix sum
    # Time O(n) as we just loop over nums once
    # Space O(min(n, modulo)) as we a hash map of size either n or modulo
    def _count_interesting_subarrays_prefix_sum(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)

        cnt_map = defaultdict(int)
        cnt_map[0] = 1
        count_interesting = 0
        prefix = 0

        # Go over all r's and see how many l's i can be an r for
        for i in range(n):
            if nums[i] % modulo == k:
                prefix += 1

            # How many l's exist before this that make it so this can be an r for an interesting subarray
            count_interesting += cnt_map[(prefix - k + modulo) % modulo]
            # Add this l as an l count
            cnt_map[prefix % modulo] += 1
    
        return count_interesting

    # Time limit exceeded
    # Time O(n^2) as we iterate over all starting and ending point combos
    # Space O(n) as we store array of size n for modulo count
    def _count_interesting_subarrays_n2(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)

        # Array for how many nums up through this one satisfy modulo == k
        count_modulo = [0] * len(nums)

        count_so_far = 0
        for i, num in enumerate(nums):
            if num % modulo == k:
                count_so_far += 1

            count_modulo[i] = count_so_far

        count_interesting = 0
        # Iterate over every starting point and see how many subarrays exist with that as the starting point
        for i in range(n):
            i_works = 0
            # Check if this singular item counts
            if nums[i] % modulo == k:
                i_works = 1

            for j in range(i, n):
                cnt = count_modulo[j] - count_modulo[i] + i_works
                if cnt % modulo == k:
                    count_interesting += 1

        return count_interesting

test_cases = [
    [3, [3,2,4], 2, 1],
    [2, [3,1,9,6], 3, 0]
]
solution = Solution()
for expected, nums, modulo, k in test_cases:
    actual = solution.countInterestingSubarrays(nums, modulo, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, modulo: {modulo}, k: {k}")

print("Ran all tests")