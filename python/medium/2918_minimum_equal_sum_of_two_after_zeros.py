from typing import List


class Solution:
    # Sum up each one and count zeros
    # return min of sum + num 0s or -1 if there are no zeros in lower one
    # Time O(n1 + n2) as we go over nums1 and nums2
    # Space O(1)
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = zeros1 = sum2 = zeros2 = 0
        for num in nums1:
            sum1 += num
            if num == 0:
                sum1 += 1
                zeros1 += 1

        for num in nums2:
            sum2 += num
            if num == 0:
                sum2 += 1
                zeros2 += 1

        # smaller one has no 0's so not possible to be equal
        if (zeros1 == 0 and sum1 < sum2) or (zeros2 == 0 and sum2 < sum1):
            return -1

        return max(sum1, sum2)
    
test_cases = [
    [12, [3,2,0,1,0], [6,5,0]],
    [-1, [2,0,2,0], [1,4]]
]
solution = Solution()
for expected, nums1, nums2 in test_cases:
    actual = solution.minSum(nums1, nums2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums1: {nums1}, nums2: {nums2}")

print("Ran all tests")