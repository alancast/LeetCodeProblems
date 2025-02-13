import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return self.minOperationsPQ(nums, k)
    
    # Create min PQ of nums, check if top is above k, if not pop top 2 and push new num
    # Time O(nlog(n))
    # Space O(n)
    def minOperationsPQ(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        numOperations = 0
        while nums[0] < k:
            num1 = heapq.heappop(nums)
            num2 = heapq.heappop(nums)
            newNum = (min(num1, num2) * 2) + max(num1, num2)
            heapq.heappush(nums, newNum)
            numOperations += 1

        return numOperations
    
testCases = [
    [[2, 11, 10, 1, 3], 10, 2],
    [[2, 11], 10, 1],
    [[11, 10], 10, 0]
]
solution = Solution()
for nums, k, expected in testCases:
    answer = solution.minOperations(nums, k)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. Inputs: k: {k}, nums: {nums}")

print("Ran all tests")