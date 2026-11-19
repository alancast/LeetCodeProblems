from heapq import nlargest, nsmallest


class Solution:
    # Just take the largest and smallest and then swap them
    # Time O(n)
    # Space O(1)
    def minimizeSum(self, nums: list[int]) -> int:
        small = nsmallest(3, nums)
        large = nlargest(3, nums)
        return min(large[0] - small[2], large[1] - small[1], large[2] - small[0])

test_cases = [
    [3, [1, 4, 7, 8, 5]],
    [0, [1, 4, 3]],
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimizeSum(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}")

print("Ran all tests")
