from typing import List


class Solution:        
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Return min number of swaps if one could make all elements in tops or bottoms equal to x.
        # returns -1 if not possible
        def minSwapsToMatch(x: int) -> int:
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
    
        n = len(tops)
        rotations = minSwapsToMatch(tops[0]) 
        # If top is possible to make match then we know either
        # 1: bottom will be impossible
        # 2: bottom will produce the same result as top for min swaps
        # So return whatever top found
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations 
        # Only needed if top couldn't produce match and top[0] and bottom[0] are different
        else:
            return minSwapsToMatch(bottoms[0])

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