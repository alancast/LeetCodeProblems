from bisect import bisect_left
from collections import Counter


class Solution:
    # Brute force would be just try for all values 0 to limit and see if min
    # But you can binary search those values to optimize
    # Time O(nlogn + LIMITlogn)
    # Space O(n)
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)

        # Keep track of sum counts as well as all mins of a pair and maxes
        sum_count = Counter()
        min_arr = []
        max_arr = []

        # Go over all pairs and find sum and min and max
        for i in range(n // 2):
            # Find which number of pair is min and max
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            sum_count[a + b] += 1
            min_arr.append(a)
            max_arr.append(b)

        # Sort the upper and lower ends
        min_arr.sort()
        max_arr.sort()

        # Set min operations to n, as in theory could modify all numbers (so upper bound)
        answer = n
        # Go over all limit values and see which one gives min
        for c in range(2, 2 * limit + 1):
            # The math portion
            add_left = (n // 2) - bisect_left(min_arr, c)
            add_right = bisect_left(max_arr, c - limit)

            current_ops = (n // 2) + add_left + add_right - sum_count[c]
            answer = min(answer, current_ops)

        return answer

test_cases = [
    [1, [1,2,4,3], 4],
    [2, [1,2,2,1], 2],
    [0, [1,2,1,2], 2]
]
solution = Solution()
for expected, nums, limit in test_cases:
    actual = solution.minMoves(nums, limit)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, limit: {limit}")

print("Ran all tests")
