from math import ceil
from typing import List


class Solution:
    # Try different values for answer with binary search
    # Find minimal one and make sure difference between high and low possible
    # Is less than 10^-6 for precision
    # Time O(nlogw) W is the range of the problem, so 10^8 here
    # Space O(1)
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        # Is it possible to have all gas stations within this distance
        def possible(D: float) -> bool:
            # Find out how many stations needed to make sure all are within D
            needed = sum(int((stations[i+1] - stations[i])/D) for i in range(len(stations) - 1))
            return needed <= k

        low = 0
        high = 10**8
        # Keep searching while bounds are wider than needed range
        while high - low > 1e-6:
            mid = (low + high) / 2.0
            # It's possible with this number, so make it smaller
            if possible(mid):
                high = mid
            else:
                low = mid

        # Round to 5 decimal places
        return round(low, 5)

test_cases = [
    [.50000, [1,2,3,4,5,6,7,8,9,10], 9],
    [14.00000, [23,24,36,39,46,56,57,65,84,98], 1]
]
solution = Solution()
for expected, stations, k in test_cases:
    actual = solution.minmaxGasDist(stations, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: stations: {stations}, k: {k}")

print("Ran all tests")