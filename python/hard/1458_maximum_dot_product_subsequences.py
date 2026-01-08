from typing import List


class Solution:
    # DP starting from end and working back to beginning
    # Time O(n*m)
    # Space O(n)
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Check for corner cases where dot product is definitely negative
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        # Now we know we can get a positive dot product, create the dp array
        m = len(nums2) + 1
        prev_dp = [0] * m
        dp = [0] * m

        # Work backwards from nums1 to start
        for i in range(len(nums1) - 1, -1, -1):
            dp = [0] * m
            # Go backwards from nums2 as well to see what to keep for max
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + prev_dp[j + 1]
                dp[j] = max(use, prev_dp[j], dp[j + 1])

            prev_dp = dp

        # Max is whatever is max possible here now
        return dp[0]

test_cases = [
    [18, [2,1,-2,5], [3,0,-6]],
    [21, [3,-2], [2,-6,7]],
    [-1, [-1,-1], [1,1]]
]
solution = Solution()
for expected, nums1, nums2 in test_cases:
    actual = solution.maxDotProduct(nums1, nums2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums1: {nums1}, nums2: {nums2}")

print("Ran all tests")
