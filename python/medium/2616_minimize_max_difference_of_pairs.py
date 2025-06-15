from typing import List


class Solution:
    # Sort nums, then pick a threshold and see how many pairs have that or less
    # Do binary search on the thresholds until we have the min
    # Time O(nlogn + nlogM) for sort plus binary search M is max diff
    # Space O(n) because sorting algorithm likely uses O(n) space
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        left = 0
        right = nums[n-1] - nums[0]
        # Happens logV times
        while left < right:
            mid = left + ((right - left) // 2) # Prevent overflow
            count_pairs = self._count_pairs_diff_less_than_threshold(mid, nums)
            if count_pairs >= p:
                right = mid
            else:
                left = mid + 1

        return left
    
    # Time O(n)
    # Space O(1)
    def _count_pairs_diff_less_than_threshold(self, threshold: int, nums: List[int]) -> int:
        n = len(nums)

        index = count = 0
        while index < n - 1:
            # If a valid pair is found, make sure to update index to skip both numbers.
            if nums[index + 1] - nums[index] <= threshold:
                count += 1
                index += 1

            index += 1

        return count

    
test_cases = [
    [1, [10,1,2,7,1,3], 2],
    [0, [4,2,1,2], 1]
]
solution = Solution()
for expected, nums, p in test_cases:
    actual = solution.minimizeMax(nums, p)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, p: {p}")

print("Ran all tests")