from collections import defaultdict
from typing import List


class Solution:
    # Go over nums twice, once for sort, once to find max with count of 1
    # Time O(n)
    # Space O(n)
    def largestUniqueNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_counts = defaultdict(int)

        # Do counts (could also just do Counter)
        for num in nums:
            num_counts[num] += 1

        # Find max with count of 1
        answer = -1
        for num, count in num_counts.items():
            if count > 1:
                continue

            answer = max(answer, num)

        return answer

    # Sort numbers and do a counter
    # Go over sorted and then first time we see one that is
    # unique from it's neighbors return it
    # Time O(nlogn) for sort
    # Space O(n) for sort
    def largestUniqueNumber_sort(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)

        for i, num in enumerate(nums):
            # Not unique if same as left
            if i > 0 and nums[i-1] == num:
                continue
            # Not unique if same as right
            if i < n - 1 and nums[i+1] == num:
                continue

            # Is largest unique
            return num

        return -1

test_cases = [
    [8, [5,7,3,9,4,9,8,3,1]],
    [-1, [9,9,8,8]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.largestUniqueNumber(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")