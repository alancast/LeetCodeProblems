from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            
        elements = sorted(points.keys())
        two_back = 0
        one_back = points[elements[0]]
        
        for i in range(1, len(elements)):
            current_element = elements[i]
            if current_element == elements[i - 1] + 1:
                # The 2 elements are adjacent, cannot take both - apply normal recurrence
                two_back, one_back = one_back, max(one_back, two_back + points[current_element])
            else:
                # Otherwise, we don't need to worry about adjacent deletions
                two_back, one_back = one_back, one_back + points[current_element]

        return one_back

testCases = [
    [[3,4,2], 6],
    [[2,2,3,3,3,4], 9]
]
implementation = Solution()
for nums, expected in testCases:
    answer = implementation.deleteAndEarn(nums)
    if answer != expected:
        print(f"FAILED TEST: Got {answer} but expected {expected}. INPUTS: {nums}")