class Solution:
    # Can be done in one pass, just store proper values
    # Time O(n)
    # Space O(1)
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)

test_cases = [
    [3, [1,2,3]],
    [0, [1,1,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minMoves(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
