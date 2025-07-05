from collections import Counter
from typing import List


class Solution:
    # Time O(n) as we go through the array once
    # Space O(n) as worst case we keep full copy of arr
    def findLucky(self, arr: List[int]) -> int:
        num_counts = Counter(arr)
        answer = -1

        for num, value in num_counts.items():
            if num == value and num > answer:
                answer = num

        return answer

test_cases = [
    [2, [2,2,3,4]],
    [3, [1,2,2,3,3,3]],
    [-1, [2,2,2,3,3]]
]
solution = Solution()
for expected, arr in test_cases:
    actual = solution.findLucky(arr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: arr: {arr}")

print("Ran all tests")