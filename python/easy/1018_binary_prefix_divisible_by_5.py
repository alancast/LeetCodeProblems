from typing import List


class Solution:
    # Just go over array and keep track of nums
    # Update entries as we go over
    # Time O(n) just go over nums once
    # Space O(1) just answer space
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)

        # Create all at once for faster memory handling
        answer = [False] * n
        total = 0
        for i, num in enumerate(nums):
            total *= 2
            total += num
            # Take mod 5 to avoid large numbers (only care about remainder)
            total = total % 5

            if total == 0:
                answer[i] = True

        return answer

test_cases = [
    [[True, False, False], [0,1,1]],
    [[False, False, False], [1,1,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.prefixesDivBy5(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")