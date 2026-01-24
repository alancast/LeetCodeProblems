from typing import List


class Solution:
    # Sort and then just pair max with min greedily
    # Time O(nlogn) for sort
    # Space O(n) for sort
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        max_sum = 0
        for i in range(n//2):
            max_sum = max(max_sum, nums[i] + nums[-(i+1)])

        return max_sum

test_cases = [
    [7, [3,5,2,3]],
    [8, [3,5,4,2,4,6]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minPairSum(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
