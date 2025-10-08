from bisect import bisect_left
from math import ceil
from typing import List


class Solution:
    # Sort potions, then do binary search for each spell to find potion cutoff
    # Time O(mlogm + nlogm)
    # Space O(m) for sort
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)

        potions.sort()

        # Go over each spell and see how many potions work with it
        answer = [0] * n
        for i in range(n):
            spell_power = spells[i]
            need = ceil(success/spell_power)
            index = bisect_left(potions, need)
            answer[i] = m - index

        return answer

test_cases = [
    [[4,0,3], [5,1,3], [1,2,3,4,5], 7],
    [[2,0,2], [3,1,2], [8,5,8], 16]
]
solution = Solution()
for expected, spells, potions, success in test_cases:
    actual = solution.successfulPairs(spells, potions, success)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: spells: {spells}, potions: {potions}, success: {success}")

print("Ran all tests")