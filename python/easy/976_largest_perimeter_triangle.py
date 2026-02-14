class Solution:
    # Sort and then just search until group of 3 where sides less than third
    # Time O(nlogn) for sort
    # Space O(n) for sort
    def largestPerimeter(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)

        # Go over all triplets until we find one that forms a triangle
        # Since it's sorted as soon as we find one we know it's max
        for i in range(n-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0

test_cases = [
    [5, [2,1,2]],
    [0, [1,2,1,10]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.largestPerimeter(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
