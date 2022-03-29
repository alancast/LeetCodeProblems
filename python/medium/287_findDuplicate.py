from typing import List


class Solution:
    # O(n) time and O(1) space
    def findDuplicate(self, nums: List[int]) -> int:
        # Flip nums at index to negative
        # If you see a negative number you know it's a dupe so return it
        for num in nums:
            index = abs(num)
            # Number has already been flipped so we found the dupe
            if nums[index] < 0:
                # Really we should break flip the numbers back because the array is modified
                # but going to comment that out for now
                return index

            nums[index] = -nums[index]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        # set duplicate where return is, then break
        # then reset numbers to original and return duplicate here
        return 0

    # O(n) time and O(n) space
    # No better time than O(n), some more complex solutions to shrink space
    def findDuplicateHash(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

testCases = [
    [[1,3,4,2,2], 2],
    [[3,1,3,4,2], 3]
]
implementation = Solution()
for nums, expected in testCases:
    answer = implementation.findDuplicate(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {nums}")