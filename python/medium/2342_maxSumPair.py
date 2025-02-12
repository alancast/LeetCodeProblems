from collections import defaultdict
from typing import List

class Solution:
    # Time O(n log(m)) space O(log(m)) where m is power of 10 of largest num, so effectively O(1)
    def maximumSum(self, nums: List[int]) -> int:
        sum_to_max_num_map = defaultdict()
        maxSum = -1
        # Loop through all the numbers
        # Find the sum of the digits
        # Compare and store values in maps
        # See if this is part of a new large sum
        # Go to next num and repeat
        for num in nums:
            digitSum = self.computeSumOfDigits(num)
            if digitSum in sum_to_max_num_map:
                tempSum = num + sum_to_max_num_map[digitSum]
                maxSum = max(tempSum, maxSum)
                if num > sum_to_max_num_map[digitSum]:
                    sum_to_max_num_map[digitSum] = num
            else:
                sum_to_max_num_map[digitSum] = num

        return maxSum
    
    def computeSumOfDigits(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += (num % 10)
            num //= 10
        
        return sum
    
testCases = [
    [[1, 2, 3, 4], -1],
    [[18, 43, 36, 13, 7], 54],
    [[10, 100, 1000], 1100],
    [[49, 85, 1000], 134],
    [[63, 72, 9, 1000], 135]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.maximumSum(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: {nums}")

print("Ran all tests")