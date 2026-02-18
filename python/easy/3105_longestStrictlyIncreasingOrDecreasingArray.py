class Solution:
    # Time O(n) have to look at all numbers
    # Space O(1)
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        longest_increase = longest_decrease = temp_increase = temp_decrease = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp_increase += 1
                longest_increase = max(longest_increase, temp_increase)
                temp_decrease = 1
            elif nums[i] < nums[i-1]:
                temp_decrease += 1
                longest_decrease = max(temp_decrease, longest_decrease)
                temp_increase = 1
            else:
                temp_decrease = temp_increase = 1

        return max(longest_increase, longest_decrease)

testCases = [
   [[1,2,3], 3],
   [[1,1,1], 1],
   [[2,2,2,2,3,6,1,1], 3]
]
solution = Solution()
for nums, expected in testCases:
   answer = solution.longestMonotonicSubarray(nums)
   if answer != expected:
      print(f"FAILED TEST: Expected {expected} but got {answer}. Input: {nums}")

print("Ran all tests")
