from math import gcd
from typing import List


class Solution:
    # If there are 1's then num operations is len(nums) - # 1s
    # If all of the nums have gcd > 1, then impossible
    # Otherwise find range where can get to 1 in smallest num
    # Time O(n^2 log M)
    # Space O(1)
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # See how many 1's there are and compute shared gcd
        shared_gcd = 0
        num_1s = 0
        for num in nums:
            if num == 1:
                num_1s += 1
            shared_gcd = gcd(shared_gcd, num)

        # If there are ones answer is found
        if num_1s > 0:
            return n - num_1s
        # If shared gcd > 1 impossible to make all ones so answer found
        if shared_gcd > 1:
            return -1

        # Find smallest length of nums where shared gcd is one
        min_len = n
        # Starting num
        for i in range(n):
            g = 0
            # Ending num
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return min_len + n - 2

test_cases = [
    [4, [2,6,3,4]],
    [-1, [2,10,6,14]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minOperations(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")