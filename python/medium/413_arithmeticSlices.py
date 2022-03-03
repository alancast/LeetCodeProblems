from typing import List


class Solution:
    # math formula of how many subsets in range
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        slices = 0
        count = 0
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                count += 1
            else:
                slices += (count * (count+1))//2
                count = 0

        # Add for slices at end
        slices += (count * (count+1))//2

        return slices

    # Dynamic programming adding up sum
    def numberOfArithmeticSlicesDP(self, nums: List[int]) -> int:
        dp = 0
        count = 0
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp += 1
                count += dp
            else:
                dp = 0

        return count

testCases = [
    [[1,2,3,4], 3],
    [[1], 0]
]
implementation = Solution()
for nums, expected in testCases:
    answer = implementation.numberOfArithmeticSlices(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {nums}")