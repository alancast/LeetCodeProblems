from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulatives = {}
        count = 0
        sum = 0
        cumulatives[sum] = 1
        for num in nums:
            sum += num
            count += cumulatives.get(sum-k, 0)
            cumulatives[sum] = cumulatives.get(sum, 0) + 1

        return count

    def subarraySum_n2(self, nums: List[int], k: int) -> int:
        count = 0
        numLength = len(nums)
        for i in range(numLength):
            tempSum = 0
            for j in range(i, numLength):
                tempSum += nums[j]
                if tempSum == k:
                    count += 1
        return count

testCases = [
    [[1], 0, 0],
    [[], 0, 0],
    [[1,1,1,-1], 2, 3],
    [[1,1,1], 2, 2],
    [[1,2,3], 3, 2]
]
solution = Solution()
for nums, k, expected in testCases:
    answer = solution.subarraySum(nums, k)
    if answer != expected:
        print(f"FAILED TEST: Got {answer} but expected {expected}. INPUTS: {nums}, {k}")