class Solution:
    # Sort array and greedily pick largest half and smallest half
    # Time O(n + nlogn)
    # Space O(n) for sort
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)

        # Transform array into squares
        for i in range(n):
            nums[i] *= nums[i]

        # Sort array
        nums.sort()

        # Return the sum of the largest half minus the sum of the smallest half
        return -sum(nums[: n // 2]) + sum(nums[n // 2 :])

test_cases = [
    [12, [1,2,3]],
    [16, [1,-1,2,-2,3,-3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxAlternatingSum(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
