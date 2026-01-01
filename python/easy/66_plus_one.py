from typing import List


class Solution:
    # Keep incrementing last digit until nothing is carried over
    # Time O(n) worst case we go over whole array
    # Space O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n-1, -1, -1):
            # If we aren't carrying something over just increment and return
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # If we get here it means that the number was all 9s
        answer = [0] * (n+1)
        answer[0] = 1
        return answer

test_cases = [
    [[1,2,4], [1,2,3]],
    [[4,3,2,2], [4,3,2,1]],
    [[1,0], [9]]
]
solution = Solution()
for expected, digits in test_cases:
    actual = solution.plusOne(digits)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: digits: {digits}")

print("Ran all tests")
