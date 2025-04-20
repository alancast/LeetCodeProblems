from collections import Counter
from typing import List


class Solution:
    # Time O(n) as loop through array (twice)
    # Space O(n) as make copy of array
    def numRabbits(self, answers: List[int]) -> int:
        num_rabbits = 0
        counts = Counter(answers)

        # They can be the same color if count is 1 more than key
        # If it's more than that must be multiple colors with same amount
        for key, value in counts.items():
            while value > key + 1:
                num_rabbits += key + 1
                value -= (key + 1)

            num_rabbits += key + 1

        return num_rabbits
    
test_cases = [
    [5, [1,1,2]],
    [3, [2,2,2]],
    [6, [2,2,2,2]],
    [11, [10,10,10]]
]
solution = Solution()
for expected, answers in test_cases:
    actual = solution.numRabbits(answers)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: answers: {answers}")

print("Ran all tests")