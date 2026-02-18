class Solution:
    # Time O(n) as we go through array once
    # Space O(1)
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        n = len(nums)
        max_diff = abs(nums[-1] - nums[0])

        for i in range(1, n):
            diff = abs(nums[i] - nums[i-1])
            max_diff = max(max_diff, diff)

        return max_diff

test_cases = [
    [3, [1,2,4]],
    [5, [-5,-10,-5]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxAdjacentDistance(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
