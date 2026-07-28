class Solution:
    # Just go over array once and store top 2
    # Time O(n)
    # Space O(1)
    def maxProduct(self, nums: list[int]) -> int:
        max_one = max_two = -1

        for num in nums:
            prev_max = max_one
            max_one = max(num, max_one)
            max_two = max(max_two, min(num, prev_max))

        return (max_one - 1) * (max_two - 1)

test_cases = [
    [12, [3,4,5,2]],
    [16, [1,5,4,5]],
    [12, [3,7]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxProduct(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
