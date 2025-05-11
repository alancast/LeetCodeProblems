from typing import List


class Solution:
    # Do binary search to find index of last neg and first positive number
    # Then math to figure out max
    # Time O(log n)
    # Space O(1)
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # Binary search to get last negative index
        last_neg_index = self._lowest_index_greater_than_x(nums, -1) - 1

        # Binary search to get first positive index
        first_pos_index = self._lowest_index_greater_than_x(nums, 0)

        return max(last_neg_index + 1, n - first_pos_index)
    
    # Time O(logn) binary search
    def _lowest_index_greater_than_x(self, nums: List[int], x: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1

        return left
        
test_cases = [
    [3, [-2,-1,-1,1,2,3]],
    [3, [-3,-2,-1,0,0,1,2]],
    [0, [0,0,0]],
    [3, [-3,-2,-1]],
    [4, [5,20,66,1314]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maximumCount(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")