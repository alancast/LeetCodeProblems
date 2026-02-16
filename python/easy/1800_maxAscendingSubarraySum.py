class Solution:
    # Time O(n) Space O(1)
    def maxAscendingSum(self, nums: list[int]) -> int:
        temp_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp_sum += nums[i]
                max_sum = max(temp_sum, max_sum)
            else:
                temp_sum = nums[i]

        return max_sum

testCases = [
    [[1, 100, 2, 3, 4], 101],
    [[10, 20, 30, 40, 50, 1, 100], 150],
    [[100], 100]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.maxAscendingSum(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. Inputs: {nums}")

print("Ran all tests")
