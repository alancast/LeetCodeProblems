from math import gcd


class Solution:
    # Just do the calculation of min and max
    # Time O(n + logM)
    # Space O(1)
    def findGCD(self, nums: list[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        return gcd(mx, mn)

test_cases = [
    [2, [2,5,6,9,10]],
    [1, [7,5,6,8,3]],
    [3, [3,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.findGCD(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
