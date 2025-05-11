from typing import List


class Solution:
    # Time O(n) as we go through the whole array
    # Space O(1)
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num & 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False
    
test_cases = [
    [False, [2,6,4,1]],
    [False, [1,2,1,1]],
    [True, [1,2,34,3,4,5,7,23,12]]
]
solution = Solution()
for expected, arr in test_cases:
    actual = solution.threeConsecutiveOdds(arr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: arr: {arr}")

print("Ran all tests")