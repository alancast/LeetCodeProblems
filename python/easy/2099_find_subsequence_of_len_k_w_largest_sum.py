from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    # Go over twice, once to find k max elements, second time to get their order
    # Can simplify by just sorting array, but that makes slower and less space efficient
    # Time O(nlogn) worst case, but realistically likely closer to O(n)
    # Space O(k)
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = [float('-inf')] * k

        # find k max nums
        for num in nums:
            if num > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, num)

        # create counter of max nums to appear
        num_counts = Counter(min_heap)

        # build answer subsequence
        answer = []
        for num in nums:
            if num in num_counts:
                answer.append(num)
                num_counts[num] -= 1
                if num_counts[num] == 0:
                    del num_counts[num]

        return answer
    
test_cases = [
    [[3,3], [2,1,3,3], 2],
    [[-1,3,4], [-1,-2,3,4], 3],
    [[3,4], [3,4,3,3], 2]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.maxSubsequence(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")