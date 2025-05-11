from heapq import heappop, heappush
from typing import List


class Solution:
    # Binary search to see min number of candies that we can give
    # Time O(nlogn)
    # Space O(1)
    def maximumCandies(self, candies: List[int], k: int) -> int:
        right = sum(candies) // k
        left = 1

        index = 0
        while left <= right:
            mid = (left + right) // 2
            if self._can_give_n_candies(candies, k, mid):
                left = mid + 1
                index = mid
            else:
                right = mid - 1
                index = right
        
        return index
    
    # Time O(n)
    def _can_give_n_candies(self, candies: List[int], k: int, n: int) -> bool:
        for num in candies:
            k -= (num // n)
        
        return k <= 0 
    
test_cases = [
    [5, [5,8,6], 3],
    [0, [2,5], 11],
    [1, [4,7,5], 16],
    [3, [4,7,5], 4]
]
solution = Solution()
for expected, candies, k in test_cases:
    actual = solution.maximumCandies(candies, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: candies: {candies}")

print("Ran all tests")