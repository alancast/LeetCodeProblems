from math import comb


class Solution:
    MOD = 10 ** 9 + 7

    # Recursive DFS
    # Time O(n^2) because we are creating new lists for each recursive call
    # Space O(n) for the recursion stack
    def numOfWays(self, nums: list[int]) -> int:

        def dfs(nums):
            m = len(nums)
            if m < 3:  # noqa: PLR2004
                return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % self.MOD

        return (dfs(nums) - 1) % self.MOD

test_cases = [
    [1, [2, 1, 3]],
    [5, [3, 4, 5, 1, 2]],
    [0, [1, 2, 3]],
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.numOfWays(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}")

print("Ran all tests")
