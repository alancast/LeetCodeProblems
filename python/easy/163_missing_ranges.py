class Solution:
    # Just go over nums and see if within range
    # Time O(n)
    # Space O(1)
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        if not nums:
            return [[lower, upper]]

        n = len(nums)
        answer = []

        # Go over all nums and create ranges
        # Check first number
        prev_num = nums[0]
        if prev_num > lower:
            answer.append([lower, prev_num - 1])

        # Go over all middle nums
        for i in range(1, n):
            num = nums[i]
            if num > lower and num <= upper and num != prev_num + 1:
                answer.append([prev_num + 1, num - 1])

            prev_num = num

        # Get last number
        if prev_num < upper:
            answer.append([prev_num + 1, upper])

        return answer

test_cases = [
    [[[0,0],[2,2],[4,49],[51,74],[76,99]], [1,3,50,75], 0, 99],
    [[[2,2],[4,49],[51,74],[76,99]], [0,1,3,50,75], 0, 99],
    [[], [-1], -1, -1]
]
solution = Solution()
for expected, nums, lower, upper in test_cases:
    actual = solution.findMissingRanges(nums, lower, upper)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, lower: {lower}, upper: {upper}")

print("Ran all tests")
