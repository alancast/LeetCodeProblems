from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result

    def findPairsNoCounter(self, nums: List[int], k: int) -> int:
        count = 0

        # just looking for duplicate numbers
        if k == 0:
            nums_set = set()
            used_nums = set()
            for num in nums:
                if num in nums_set and num not in used_nums:
                    count += 1
                    used_nums.add(num)

                nums_set.add(num)
            
            return count

        nums_set = set()
        for num in nums:
            nums_set.add(num)
        
        count = 0
        used_nums = set()
        for num in nums:
            if num + k in nums_set and num not in used_nums:
                count += 1
                used_nums.add(num)

        return count

testCases = [
    [[3,1,4,1,5], 2, 2],
    [[], 2, 0],
    [[1,1], 0, 1],
    [[1,1,1], 0, 1],
    [[1,2,3,4,5], 1, 4],
    [[1,3,1,5,4], 0, 1]
]
solution = Solution()
for nums, k, expected in testCases:
    answer = solution.findPairs(nums, k)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Input: {nums}, {k}")