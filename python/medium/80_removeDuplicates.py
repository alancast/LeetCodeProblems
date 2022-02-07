from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        previousNum = nums[0]
        count = 1
        indexSubtractor = 0
        n = len(nums)
        i = 1
        
        while i < n:
            num = nums[i]
            if num == previousNum:
                count += 1
                # We have too many of this num so start removing it
                while count == 3 and i < n-1:
                    i += 1
                    indexSubtractor += 1
                    num = nums[i]
                    if num != previousNum:
                        count = 1
            else:
                count = 1
            
            previousNum = num
            nums[i-indexSubtractor] = num
            i += 1

        # We were over the count at the end of the list
        if count == 3:
            indexSubtractor += 1

        return n - indexSubtractor
    
testCases = [
    [[1,1,1,2,2,3], 5],
    [[1,1,1], 2],
    [[0,0,1,1,1,1,2,3,3], 7],
    [[], 0]
]
solution = Solution()
for nums, expected in testCases:
    numsCopy = nums.copy()
    answer = solution.removeDuplicates(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}")
        print(f"Input: {numsCopy}. Returned {nums}")