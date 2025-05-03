from typing import List


class Solution:
    # Time O(n) as we iterate through top at most twice
    # Space O(1) as we don't keep any extra
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        rotations = self._min_swaps_to_match(tops[0], tops, bottoms)

        # If top and bottom are same number then we have our answer
        # If they are different numbers but top returned an answer
        # That means bottom number would require the exact same amount of swaps
        # So also return to top
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations 
        # Only needed if top couldn't produce match and top[0] and bottom[0] are different
        else:
            return self._min_swaps_to_match(bottoms[0], tops, bottoms)
        
    # Return min number of swaps if one could make all elements in tops or bottoms equal to x.
    # returns -1 if not possible
    def _min_swaps_to_match(self, x: int, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        rotations_top = rotations_bottom = 0
        for i in range(n):
            # Impossible to match
            if tops[i] != x and bottoms[i] != x:
                return -1
            elif tops[i] != x:
                rotations_top += 1
            elif bottoms[i] != x:
                rotations_bottom += 1

        return min(rotations_top, rotations_bottom)

testCases = [
    [[2,1,2,4,2,2], [5,2,6,2,3,2], 2],
    [[5,2,5,2,5,2,2], [2,5,2,5,2,5,5], 3],
    [[5,2,5,2,5,2,2], [2,5,2,5,2,5,5], 3],
    [[3,5,1,2,3], [3,6,3,3,4], -1]
]
implementation = Solution()
for tops, bottoms, expected in testCases:
    answer = implementation.minDominoRotations(tops, bottoms)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: tops: {tops} bottoms: {bottoms}")