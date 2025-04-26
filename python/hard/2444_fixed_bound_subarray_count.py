from typing import List


class Solution:
    # Time O(n) as we just go through the subarray once
    # Space O(1)
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = 0
        min_index = max_index = -1
        count = 0

        for i, num in enumerate(nums):
            # breaks any sub arrays
            if num < minK or num > maxK:
                min_index = max_index = -1
                left = i + 1
                continue

            # Update indexes
            if num == minK:
                min_index = i
            if num == maxK:
                max_index = i

            # This can be included in a sub array
            if min_index >= 0 and max_index >= 0:
                max_low_index = min(min_index, max_index)
                # How many subarrays can end here
                count += max_low_index - left + 1

        return count
    
test_cases = [
    [1, [4,3], 3, 3],
    [2, [1,3,5,2,7,5], 1, 5],
    [10, [1,1,1,1], 1, 1]
]
solution = Solution()
for expected, nums, minK, maxK in test_cases:
    actual = solution.countSubarrays(nums, minK, maxK)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, minK: {minK}, maxK: {maxK}")

print("Ran all tests")