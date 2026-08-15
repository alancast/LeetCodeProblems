class Solution:
    # DP. Compute suffix sum (how many stones are left)
    # Work backwards and take from that
    # Time O(n^3)
    # Space O(n^2)
    def stoneGameII(self, piles: list[int]) -> int:
        length = len(piles)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        # Store suffix sum for all possible suffix
        suffix_sum = [0 for _ in range(length + 1)]
        for i in range(length - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Initialize the dp array.
        for i in range(length + 1):
            # If you can take all the stones that are left at this iteration
            dp[i][length] = suffix_sum[i]

        # Work backwards from end to start
        # Start from the last index to store the future state first.
        for index in range(length - 1, -1, -1):
            # Compute what max before this would be
            for max_till_now in range(length - 1, 0, -1):
                for X in range(1, min(2 * max_till_now, length - index) + 1):
                    # Compute DP for all values of x
                    dp[index][max_till_now] = max(
                        dp[index][max_till_now],
                        suffix_sum[index] - dp[index + X][max(max_till_now, X)],
                    )

        # What's the max that can be taken at turn 0 with length 1
        return dp[0][1]

test_cases = [
    [10, [2,7,9,4,4]],
    [104, [1,2,3,4,5,100]]
]
solution = Solution()
for expected, piles in test_cases:
    actual = solution.stoneGameII(piles)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: piles: {piles}")

print("Ran all tests")
