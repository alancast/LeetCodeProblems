from typing import List


class Solution:
    # Create set of nums and then just check set
    # Time O(n) as we go over nums once then O(1) for checking
    # Space O(n) as we convert nums to set
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)

        while original in num_set:
            original *= 2

        return original

test_cases = [
    [24, [5,3,6,1,12], 3],
    [4, [2,7,9], 4]
]
solution = Solution()
for expected, nums, original in test_cases:
    actual = solution.findFinalValue(nums, original)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, original: {original}")

print("Ran all tests")