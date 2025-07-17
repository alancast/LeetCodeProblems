from typing import List


class Solution:
    # Time O(k^2 + nk) k^2 for creating dp, then nk for finding max
    # Space O(k^2) for dp array
    def maximumLength(self, nums: List[int], k: int) -> int:
        # For a sequence we need x y and y x to have the same mod k
        # dp to store modulo cur, prev
        dp = [[0] * k for _ in range(k)]
        answer = 0

        # Go over and do computations
        for num in nums:
            # Find this num mod k
            curr = num % k

            # Increment sequence lengths for this mod
            for prev in range(k):
                # Increase sequence length then see if it's the new longest one
                dp[prev][curr] = dp[curr][prev] + 1
                answer = max(answer, dp[prev][curr])

        return answer
    
test_cases = [
    [5, [1,2,3,4,5], 2],
    [4, [1,4,2,3,1,4], 3]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.maximumLength(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")