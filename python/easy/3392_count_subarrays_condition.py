class Solution:
    # Time O(n) as we go over nums once
    # Space O(1)
    def countSubarrays(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n-2):
            if (2 * (nums[i] + nums[i+2])) == nums[i+1]:
                count += 1

        return count

test_cases = [
    [1, [1,2,1,4,1]],
    [0, [1,1,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.countSubarrays(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
