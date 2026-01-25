from typing import List


class Solution:
    # Sort then just go over array and compute apart
    # Time O(nlogn) for sort
    # Space O(n) for sort
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()

        min_diff = float('inf')
        for i in range(n - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return int(min_diff)

test_cases = [
    [0, [90], 1],
    [2, [9,4,1,7], 2]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.minimumDifference(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
