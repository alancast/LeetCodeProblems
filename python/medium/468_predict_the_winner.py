class Solution:
    # Dynamic programming space optimized (non space optimized below)
    # Think of a n by n dp array where diagonal is round 1
    # Then moving one off the diagonal based on the left and below is next round
    # Eventually at top right corner you have final round
    # To Space optimize you only need to store the last row (diagonal)
    # Time O(n^2)
    # Space O(n)
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        # Go over each round
        for diff in range(1, n):
            # Go along diagonal
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])

        return dp[0] >= 0

    # The non space optimized DP
    # Time O(n^2)
    # Space O(n^2)
    def predictTheWinner_dp(self, nums: list[int]) -> bool:
        n = len(nums)

        # Initialize DP array and fill diagonal with starting numbers
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        # Go over each round and move off diagonal
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                # Each one is a choice of the item to the left or the item below, which one to take and leave other for opp
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])

        return dp[0][n - 1] >= 0

test_cases = [
    [False, [1,5,2]],
    [True, [1,5,233,7]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.predictTheWinner(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
