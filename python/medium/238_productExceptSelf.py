from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        answer = [1] * N
        for i in range(1,N):
            answer[i] = nums[i-1] * answer[i-1]   

        right = 1
        for i in reversed(range(N)):
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer

    def productExceptSelf_O_N_space(self, nums: List[int]) -> List[int]:
        N = len(nums)

        prefix = [1] * N
        for i in range(1,N):
            prefix[i] = nums[i-1] * prefix[i-1]

        suffix = [1] * N
        for i in range(N-2,-1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]     

        answer = [1] * N
        for i in range(N):
            answer[i] = prefix[i] * suffix[i]

        return answer

testCases = [
    [[1,2,3,4], [24,12,8,6]],
    [[], []],
    [[2,2], [2,2]],
    [[1,1], [1,1]],
    [[-1,1,0,-3,3], [0,0,9,0,0]]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.productExceptSelf(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Input: {nums}")