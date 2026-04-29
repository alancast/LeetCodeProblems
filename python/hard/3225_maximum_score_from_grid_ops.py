class Solution:
    # DP over (current column height, previous column height) pairs
    # At each column boundary the shorter column earns its cells in the gap zone between the two heights
    # prev_max and prev_suffix_max precompute running maxima to cut transitions from O(n^4) to O(n^3)
    # Time O(n^3) where n is the number of columns
    # Space O(n^2)
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        if n == 1:
            return 0

        # Compute sum of columns
        # col_sum[c][r] = sum of top r cells in column c
        col_sum = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        # dp[curr_h][prev_h] = best score so far where current column has height curr_h
        # and the column to its left has height prev_h
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # prev_max[h][k] = max over p in 0..k of dp[h][p] adjusted by boundary penalty
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        # prev_suffix_max[h][k] = max over p in k..n of dp[h][p]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]

        # Iterate over columns from left to right, building the DP for each new column
        for i in range(1, n):
            new_dp = [[0] * (n + 1) for _ in range(n + 1)]
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        # Shorter current column earns its own cells in the gap between curr_h and prev_h
                        extra_score = col_sum[i][prev_h] - col_sum[i][curr_h]
                        new_dp[curr_h][prev_h] = max(
                            new_dp[curr_h][prev_h],
                            prev_suffix_max[prev_h][0] + extra_score,
                        )
                    else:
                        # Taller current column exposes the previous column's cells from prev_h up to curr_h
                        extra_score = (
                            col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        )
                        new_dp[curr_h][prev_h] = max(
                            new_dp[curr_h][prev_h],
                            prev_suffix_max[prev_h][curr_h],
                            prev_max[prev_h][curr_h] + extra_score,
                        )

            dp = new_dp

            # Rebuild prefix and suffix maxima tables for the next column's transitions
            for curr_h in range(n + 1):
                prev_max[curr_h][0] = dp[curr_h][0]
                for prev_h in range(1, n + 1):
                    # Subtract the score the next column would add for prev_h > curr_h so
                    # prev_max stays comparable across all future curr_h lookups
                    penalty = (
                        col_sum[i][prev_h] - col_sum[i][curr_h]
                        if prev_h > curr_h
                        else 0
                    )
                    prev_max[curr_h][prev_h] = max(
                        prev_max[curr_h][prev_h - 1],
                        dp[curr_h][prev_h] - penalty,
                    )

                prev_suffix_max[curr_h][n] = dp[curr_h][n]
                for prev_h in range(n - 1, -1, -1):
                    prev_suffix_max[curr_h][prev_h] = max(
                        prev_suffix_max[curr_h][prev_h + 1],
                        dp[curr_h][prev_h],
                    )

        # The last column must have height 0 or n to correctly bound the rightmost gap score
        answer = 0
        for k in range(n + 1):
            answer = max(answer, dp[n][k], dp[0][k])

        return answer

test_cases = [
    [11, [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]],
    [94, [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.maximumScore(grid)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")
