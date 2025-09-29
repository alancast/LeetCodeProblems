from typing import List


class Solution:
    # Go over array once. Find num with the highest count.
    # Make sure count * k less than len(nums)
    # Time O(n)
    # Space O(1)
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        max_count_limit = n//k

        curr_count = 0
        prev_num = nums[0]
        for num in nums:
            if num == prev_num:
                curr_count += 1
                if curr_count > max_count_limit:
                    return False
            else:
                curr_count = 1
            
            prev_num = num

        return True

test_cases = [
    [True, [1,2,2,3,3,4,4], 3],
    [False, [5,6,6,7,8], 3]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.canDivideIntoSubsequences(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")