class Solution:
    # DP approach to count the number of non-empty subarrays with product
    # modulo k equal to each possible remainder
    # Time O(nk)
    # Space O(k)
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        answer = [0] * k

        # Initial state: no elements have been processed, so no non-empty subarray exists
        dp = [0] * k

        # Go over whole array and update the dp state for each number
        for i in range(n):
            # Current state (rolling array).
            next_dp = [0] * k

            next_dp[nums[i] % k] += 1

            for r in range(k):
                next_dp[(r * nums[i]) % k] += dp[r]

            # Update the state.
            dp = next_dp

            # Accumulate the answer.
            for r in range(k):
                answer[r] += dp[r]

        return answer

test_cases = [
    [[9,2,4], [1,2,3,4,5], 3],
    [[18,1,2,0], [1,2,4,8,16,32], 4],
    [[9,6], [1,1,2,1,1], 2]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.resultArray(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
