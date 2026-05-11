class Solution:
    NEG_INF = -10000000

    # Dynamic programming, max to get from index 0 to i
    # Formula is at each index go from start to this and update max
    # Time O(n^2)
    # Space O(n)
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)

        # Initialize every entry to negative inf
        dp = [Solution.NEG_INF] * n
        # Set start to 0 max jumps
        dp[0] = 0

        # Go over all ending indexes until end
        for i in range(1, n):
            for j in range(i):
                # If possible to jump to i from j check if it's a new max
                if abs(nums[j] - nums[i]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return -1 if dp[n - 1] < 0 else dp[n - 1]

test_cases = [
    [3, [1,3,6,4,1,2], 2],
    [5, [1,3,6,4,1,2], 3],
    [-1, [1,3,6,4,1,2], 0]
]
solution = Solution()
for expected, nums, target in test_cases:
    actual = solution.maximumJumps(nums, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, target: {target}")

print("Ran all tests")
