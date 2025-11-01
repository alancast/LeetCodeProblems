from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from typing import List


class Solution:
    # Optimized version of the sorted one
    # Where we prune numbers in range that can't yield answer
    # Sort the array and try each value in pruned range [min, max]
    # And see how many nums it's possible to get from each value
    # Time O(nlogn)
    # Space O(n) for sort and possible answer nums array
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        # Create set of all possible numbers that could be answer
        num_count = defaultdict(int)
        possible_answer_nums = set()

        # Create tighter bounds on possible answer nums.
        # Only consider a number and thing within +- k of it
        # E.g. if array is 1, 999, and k is 1 we don't care about 3 - 997
        def add_possible_answer_num(num: int) -> None:
            # We already added this number
            if num in possible_answer_nums:
                return

            possible_answer_nums.add(num)
            if num - k >= nums[0]:
                possible_answer_nums.add(num - k)
            if num + k <= nums[-1]:
                possible_answer_nums.add(num + k)

        # Get num count of all numbers and create possible answers
        for num in nums:
            num_count[num] += 1
            add_possible_answer_num(num)

        # Go over all possible nums and get answer
        answer = 0
        for num in sorted(possible_answer_nums):
            # Find leftmost index that could be num
            l = bisect_left(nums, num - k)
            # Find rightmost index that could be num
            r = bisect_right(nums, num + k) - 1

            # Find how many nums could be converted to this after operation
            # If this num is in the array that makes the potential higher
            # Otherwise it's just the full range of indexes found above
            if num in num_count:
                temp_answer = min(r - l + 1, num_count[num] + numOperations)
            else:
                temp_answer = min(r - l + 1, numOperations)

            answer = max(answer, temp_answer)

        return answer

    # Use prefix sum to do in linear time
    # Time O(n + max)
    # Space O(max)
    def maxFrequency_linear(self, nums: List[int], k: int, numOperations: int) -> int:
        # Find max num (Add 1 for bound checking)
        max_val = max(nums) + 1

        # Create and populate prefix sum count array
        prefix_sum_count = [0] * max_val
        for num in nums:
            prefix_sum_count[num] += 1
        for i in range(1, max_val):
            prefix_sum_count[i] += prefix_sum_count[i - 1]

        # Go over all values in range and see how many can be made this
        answer = 0
        for i in range(max_val):
            # Find left and right bound ranges
            left = max(0, i - k)
            right = min(max_val - 1, i + k)

            # How many total are in the range
            total = prefix_sum_count[right] - (prefix_sum_count[left - 1] if left else 0)
            # How many times does this num occur
            freq = prefix_sum_count[i] - (prefix_sum_count[i - 1] if i else 0)
            # How many can be made this num
            answer = max(answer, freq + min(numOperations, total - freq))

        return answer

    # Sort the array and try each value in range [min, max]
    # And see how many nums it's possible to get from each value
    # Time O(nlogn + n + range*logn) for sort->counter->range check
    # Space O(n) for sort
    def maxFrequency_sorted(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        answer = 0

        # Keep count of how many times a number is in the array
        num_count = Counter(nums)

        # Go over all possible nums
        for num in range(nums[0], nums[-1] + 1):
            # Find leftmost index that could be num
            l = bisect_left(nums, num - k)
            # Find rightmost index that could be num
            r = bisect_right(nums, num + k) - 1

            # Find how many nums could be converted to this after operation
            # If this num is in the array that makes the potential higher
            # Otherwise it's just the full range of indexes found above
            if num in num_count:
                temp_answer = min(r - l + 1, num_count[num] + numOperations)
            else:
                temp_answer = min(r - l + 1, numOperations)

            answer = max(answer, temp_answer)

        return answer

test_cases = [
    [2, [1,4,5], 1, 2],
    [2, [5,11,20,20], 5, 1]
]
solution = Solution()
for expected, nums, k, num_operations in test_cases:
    actual = solution.maxFrequency(nums, k, num_operations)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}, numOperations: {num_operations}")

print("Ran all tests")