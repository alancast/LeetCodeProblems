class Solution:
    # Check every subarray and keep the smallest positive sum in the given length range.
    # Time O(nr)
    # Space O(1)
    def minimumSumSubarray(self, nums: list[int], left: int, right: int) -> int:
        n = len(nums)
        min_sum = None

        # Try each starting index and extend the subarray up to length right.
        for start in range(n):
            subarray_sum = 0
            for end in range(start, min(n, start + right)):
                subarray_sum += nums[end]
                subarray_length = end - start + 1

                # Keep the sum if the subarray is in range and positive.
                if left <= subarray_length and subarray_sum > 0:
                    min_sum = (
                        subarray_sum
                        if min_sum is None
                        else min(min_sum, subarray_sum)
                    )

        return -1 if min_sum is None else min_sum

test_cases = [
    [1, [3, -2, 1, 4], 2, 3],
    [-1, [-2, 2, -3, 1], 2, 3],
    [3, [1, 2, 3, 4], 2, 4],
]
solution = Solution()
for expected, nums, left, right in test_cases:
    actual = solution.minimumSumSubarray(nums, left, right)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, l: {left}, r: {right}")

print("Ran all tests")
