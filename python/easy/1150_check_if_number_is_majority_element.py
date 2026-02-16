from bisect import bisect_left


class Solution:
    # Optimized binary search method where we just check it once
    # Find first index then add length//2 and make sure it's still target
    # Time O(logn)
    # Space O(1)
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        half = n//2

        # Find first index of target
        before_index = bisect_left(nums, target)

        # Make sure target is before half
        if before_index + half >= n:
            return False

        # Make first index + half is still target
        return nums[before_index + half] == target

    # Do binary search of number one larger and number itself
    # Compute difference in insertion index and see if majority
    # Time O(logn)
    # Space O(1)
    def isMajorityElement_binary_search(self, nums: list[int], target: int) -> bool:
        n = len(nums)

        # Find first index of target
        before_index = bisect_left(nums, target)
        # Find first index after target
        after_index = bisect_left(nums, target + 1)

        # Make sure over half the list is target
        return (after_index - before_index) > (n//2)

test_cases = [
    [True, [2,4,5,5,5,5,5,6,6], 5],
    [False, [10,100,101,101], 101],
    [True, [10,100,101,101,101], 101]
]
solution = Solution()
for expected, nums, target in test_cases:
    actual = solution.isMajorityElement(nums, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, target: {target}")

print("Ran all tests")
