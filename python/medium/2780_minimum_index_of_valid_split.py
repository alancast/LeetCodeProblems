from collections import defaultdict
from typing import List


class Solution:
    # Time O(n) go through nums three times
    # Space O(1) don't need hash map by taking advantage of Boyer-Moore Majority voting
    def minimumIndex(self, nums: List[int]) -> int:
        # Find the majority element
        majority = nums[0]
        count = 0
        majority_count = 0
        n = len(nums)
        for num in nums:
            if num == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority = num
                count = 1

        # Now that we have the majority element count it's frequency
        for num in nums:
            if num == majority:
                majority_count += 1

        # Go through nums and at each index check if split is valid
        count = 0
        remaining_count = majority_count
        for i, num in enumerate(nums):
            if num == majority:
                count += 1
                remaining_count -= 1

            if (count * 2) > (i + 1) and (remaining_count * 2) > (n - i - 1):
                return i

        return -1

    # Time O(n) go through nums at most twice
    # Space O(n) to find max num we store map which can be size n
    def minimumIndex_hash_map(self, nums: List[int]) -> int:
        max_num = max_count = 0
        num_counts = defaultdict(int)

        # Find maximum num
        for num in nums:
            num_counts[num] += 1
            if num_counts[num] > max_count:
                max_count = num_counts[num]
                max_num = num

        # Go through nums and at each index check if split is valid
        n = len(nums)
        used = 0
        left = max_count
        for i, num in enumerate(nums):
            if num == max_num:
                used += 1
                left -= 1
                
            # Check if valid index
            if used > ((i+1)//2) and left > ((n-(i+1))//2):
                return i

        return -1
    
test_cases = [
    [2, [1,2,2,2]],
    [4, [2,1,3,1,1,1,7,1,2,1]],
    [-1, [3,3,3,3,7,2,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumIndex(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")