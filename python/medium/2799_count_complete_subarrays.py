from collections import Counter, defaultdict
from typing import List


class Solution:
    # Two pointers. Go through list once, see how many distinct numbers there are
    # Then move left pointer and see when a complete subarray starts for that pointer
    # Then keep counting as left continues
    # Time O(n) as we go over nums multiple times but have O(1) operations each time
    # Space O(n) as we store hash map
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Find num distinct
        num_counts = Counter(nums)
        num_distinct = len(num_counts)

        # Iterate over starting indexes and find how many complete subarrays at each one
        n = len(nums)
        left = right = count = 0
        nums_included = defaultdict(int)
        while left < n:
            # Find first right entry that matches distinct num
            while len(nums_included) < num_distinct and right < n:
                nums_included[nums[right]] += 1
                right += 1

            # We now either have the num distinct or have reached the end
            # If we've reached the end break out of the loops
            if len(nums_included) < num_distinct:
                break

            # Add the count of this sub_array plus all ones after it
            count += n - right + 1

            # Move left forward and remove that entry
            nums_included[nums[left]] -= 1
            if nums_included[nums[left]] == 0:
                del nums_included[nums[left]]

            left += 1

        return count

test_cases = [
    [4, [1,3,1,2,2]],
    [10, [5,5,5,5]],
    [1, [1,2,3,4]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.countCompleteSubarrays(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")