class Solution:
    # Make sure numbers only lower once, and end of array is less than start if lowered
    # Time O(n), space O(1)
    def check(self, nums: list[int]) -> bool:
        previousNum = firstNum = nums[0]
        lowered = False
        for i in range(1,len(nums)):
            currentNum = nums[i]
            if currentNum < previousNum:
                # The array has already lowered once, so this is a second time which means not sorted
                if lowered:
                    return False

                lowered = True

            previousNum = currentNum

        return not lowered or previousNum <= firstNum

testCases = [
    [[3,4,5,1,2], True],
    [[3,5,4], False],
    [[3,5,3], True],
    [[2,1,3,4], False],
    [[1,2,3], True]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.check(nums)
    if answer != expected:
        print(f"TEST FAILED: Expected {expected} but got {answer}. Input: {nums}")

print("Ran all tests")
