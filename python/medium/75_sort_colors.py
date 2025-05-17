from typing import List


class Solution:
    # Time O(n) go through once
    # Space O(1) 
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # Pointer to current evaluating index as well as next 0 location
        p0 = curr = 0

        # Pointer for where to place next 2
        p2 = len(nums) - 1

        # Go through and evaluate and swap until it's sorted
        while curr <= p2:
            # Swap p0 num with the 0 and increment counts
            if nums[curr] == 0:
                nums[curr] = nums[p0]
                nums[p0] = 0
                p0 += 1
                curr += 1
            # Swap p2 num with 2 and change counts
            elif nums[curr] == 2:
                nums[curr] = nums[p2]
                nums[p2] = 2
                p2 -= 1
            # Curr is a 1 so no swaps needed
            else:
                curr += 1

    # Time O(n) go through and count then go through and overwrite
    # Space O(1) 
    def sortColors_two_pass(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_count = white_count = blue_count = 0
        for num in nums:
            if num == 0:
                red_count += 1
            elif num == 1:
                white_count += 1
            else:
                blue_count += 1

        for i in range(len(nums)):
            if red_count > 0:
                nums[i] = 0
                red_count -= 1
            elif white_count > 0:
                nums[i] = 1
                white_count -= 1
            else:
                nums[i] = 2

        
test_cases = [
    [[0,0,1,1,2,2], [2,0,2,1,1,0]],
    [[0,1,2], [2,0,1]]
]
solution = Solution()
for expected, nums in test_cases:
    solution.sortColors(nums)
    if expected != nums:
        print(f"FAILED TEST! Expected {expected} but got {nums}. INPUTS: nums: {nums}")

print("Ran all tests")