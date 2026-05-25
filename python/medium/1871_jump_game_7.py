class Solution:
    # Can't do greedy because could over jump solution
    # Instead do DP and prefix sum
    # Time O(n)
    # Space O(n)
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # Stores 0 if can't get there, 1 if can
        dp = [0] * n
        prefix_sum = [0] * n
        dp[0] = 1

        # Start dynamic programming from i=minJump
        # So precompute the prefix sums for the part [0, minJump)
        for i in range(minJump):
            prefix_sum[i] = 1

        # Now go til end of s and see if you can get there
        for i in range(minJump, n):
            left = i - maxJump
            right = i - minJump

            # Update if possible to get there when we see a 0
            if s[i] == "0":
                total = prefix_sum[right] - (0 if left <= 0 else prefix_sum[left - 1])
                dp[i] = int(total != 0)

            prefix_sum[i] = prefix_sum[i - 1] + dp[i]

        return bool(dp[n - 1])

test_cases = [
    [False, "00111010", 3, 5],
    [True, "011010", 2, 3],
    [False, "01101110", 2, 3]
]
solution = Solution()
for expected, s, min_jump, max_jump in test_cases:
    actual = solution.canReach(s, min_jump, max_jump)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, min_jump: {min_jump}, max_jump: {max_jump}")

print("Ran all tests")
