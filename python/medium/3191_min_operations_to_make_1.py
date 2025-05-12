from typing import List


class Solution:
    # Time O(n) as we just go over nums once
    # Space O(1)
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        flips = 0
        flip_map = {0: 1, 1: 0}
        for i in range(n - 2):
            num = nums[i]
            if num == 0:
                flips += 1
                nums[i] = 1
                nums[i+1] = flip_map[nums[i+1]]
                nums[i+2] = flip_map[nums[i+2]]

        # Make sure last nums are 1's
        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return flips
    
test_cases = [
    [3, [0,1,1,1,0,0]],
    [-1, [0,1,1,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minOperations(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")