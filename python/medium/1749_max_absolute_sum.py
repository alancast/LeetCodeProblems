from typing import List

class Solution:
    # Time O(n) goes through nums once
    # Space O(1)
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positive_sum = negative_sum = answer = 0
        for num in nums:
            positive_sum = max(0, positive_sum + num)
            negative_sum = min(0, negative_sum + num)
            answer = max(answer, positive_sum, abs(negative_sum))

        return answer
    
    # Time O(n) goes through nums once
    # Space O(1)
    def maxAbsoluteSum_prefix_sums(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

        return max_prefix_sum - min_prefix_sum
    
test_cases = [
    [44, [-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]],
    [14, [7,-4,-2,-2,-6]],
    [5, [1,-3,2,3,-4]],
    [8, [2,-5,1,-4,3,-2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxAbsoluteSum(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")