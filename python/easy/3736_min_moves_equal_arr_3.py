class Solution:
    # Get max then compute diff
    # Time O(n)
    # Space O(1)
    def minMoves(self, nums: list[int]) -> int:
        max_num = max(nums)
        return sum(max_num - x for x in nums)

test_cases = [
    [3, [2,1,3]],
    [2, [4,4,5]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minMoves(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
