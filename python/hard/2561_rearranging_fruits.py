from collections import Counter
from typing import List


class Solution:
    # Time O(nlogn) as sorting imbalanced fruits array is nlogn worst case
    # Space O(n) as full baskets could be imbalanced
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)

        # Create count of nums in each basket
        # Must be even across the two otherwise they can't be equal
        num_frequency_diffs = Counter()
        # Also find min fruit value in baskets
        min_num = float('inf')
        for i in range(n):
            num1 = basket1[i]
            num2 = basket2[i]
            # Arbitrarily pick basket1 as the positive one
            num_frequency_diffs[num1] += 1
            num_frequency_diffs[num2] -= 1

            min_num = min(min_num, num1, num2)

        # Create list of basket imbalances for things that can be merged
        imbalanced_fruits = []
        for key, count in num_frequency_diffs.items():
            # Make sure all fruits have even number of counts
            if count % 2 == 1:
                return -1
            
            # Add this number count/2 times as it must be swapped that many times
            imbalanced_fruits.extend([key] * (abs(count) // 2))

        # Baskets are already equal so no need to swap
        if not imbalanced_fruits:
            return 0
        
        # Sort imbalanced_fruits and start greedily swapping
        imbalanced_fruits.sort()
        # Can either swap by swapping x1 with x2 (with a cost of min x1, x2)
        # Or do an indirect swap by swapping x1 with min and x2 with min (cost 2*min)
        answer = 0

        # Go over first half of array and make swaps
        m = len(imbalanced_fruits)
        for i in range(m//2):
            num = imbalanced_fruits[i]
            answer += min(num, 2*min_num)

        return answer
    
test_cases = [
    [1, [4,2,2,2], [1,4,1,2]],
    [-1, [2,3,4,1], [3,2,5,1]]
]
solution = Solution()
for expected, basket1, basket2 in test_cases:
    actual = solution.minCost(basket1, basket2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: basket1: {basket1}, basket2: {basket2}")

print("Ran all tests")