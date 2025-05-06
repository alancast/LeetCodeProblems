from typing import List


class Solution:
    # If space is crazzzzzy tight can also do in place by going over array twice
    # First time by doing x * (num % x) and second time by doing // x
    # Time O(n) as we go through the whole array once
    # Space O(1) as the only space we have is the answer
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        for i in range(n):
            answer[i] = nums[nums[i]]

        return answer
    
test_cases = [
    [[0,1,2,4,5,3], [0,2,1,5,3,4]],
    [[4,5,0,1,2,3], [5,0,1,2,3,4]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.buildArray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")