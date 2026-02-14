class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            num = nums[mid]
            if num < target:
                left = mid + 1
            elif num > target:
                right = mid - 1
            else:
                return mid

        return -1

testCases = [
    [[-1,0,3,5,9,12], 9, 4],
    [[-1,0,3,5,9,12], -1, 0],
    [[-1,0,3,5,9,12], 12, 5],
    [[-1,0,3,5,9,12], 2, -1]
]
implementation = Solution()
for nums, target, expected in testCases:
    answer = implementation.search(nums, target)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: nums: {nums} target: {target}")

print("Ran all tests")
