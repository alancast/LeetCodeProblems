from collections import defaultdict
from typing import List


class Solution:
    # Hash map and two pointers constantly calculating sum
    # Time O(n) as we go over the whole list once (twice cuz 2 pointers)
    # Space O(n) as worst case full array is in map
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = total = answer = 0
        num_counts = defaultdict(int)

        # Go over each number and add it to the subarray
        # And see if we have a dupe
        for right in range(n):
            # Add new num
            new_num = nums[right]
            num_counts[new_num] += 1
            total += new_num

            # If new num already in there remove it's older one
            while num_counts[new_num] > 1:
                old_num = nums[left]
                total -= old_num
                num_counts[old_num] -= 1
                left += 1

            answer = max(answer, total)

        return answer
    
test_cases = [
    [17, [4,2,4,5,6]],
    [8, [5,2,1,2,5,2,1,2,5]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maximumUniqueSubarray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")