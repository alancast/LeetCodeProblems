from heapq import heappop, heappush
from typing import List


class Solution:
    # Keep a queue of most negative numbers, when we go negative move the biggest num to the back
    # Time O(n log(n)) as worst case it's 1 positive number and the other n are all negative
    # Space O(n) as worst case it's 1 positive number and the other n are all negative
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        negative_nums_heap = []
        prefix_sum = count = 0

        for num in nums:
            prefix_sum += num

            if num < 0:
                heappush(negative_nums_heap, num)

            # If prefix sum is negative effectively move the biggest negative num to the back
            if prefix_sum < 0:
                count += 1
                negative_popped = heappop(negative_nums_heap)
                prefix_sum -= negative_popped

        return count
    
test_cases = [
    [0, [2,3,-5,4]],
    [0, [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]],
    [1, [5,-4,-2,-2,1]],
    [1, [3,-5,-2,6]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.makePrefSumNonNegative(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")