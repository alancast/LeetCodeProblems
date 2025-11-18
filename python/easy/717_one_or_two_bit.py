from typing import List


class Solution:
    # Go over all chars skipping 1 every time we see a 1
    # Time O(n)
    # Space O(1)
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        
        i = 0
        last_one_digit = False
        while i < n:
            if bits[i] == 1:
                i += 2
                last_one_digit = False
            else:
                i += 1
                last_one_digit = True

        return last_one_digit

test_cases = [
    [True, [1,0,0]],
    [True, [1,1,0]],
    [True, [1,0,0,0]],
    [False, [1,1,1,0]]
]
solution = Solution()
for expected, bits in test_cases:
    actual = solution.isOneBitCharacter(bits)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: bits: {bits}")

print("Ran all tests")