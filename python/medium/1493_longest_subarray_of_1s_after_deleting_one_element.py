from typing import List


class Solution:
    # Keep pointer to left and last zero, compute max width
    # Time O(n) as the array is gone over once
    # Space O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        left = answer = 0
        last_zero = -1
        # Set this to one if we see a zero. Only used to see if string is all ones
        zero_included = 0

        for i, num in enumerate(nums):
            if num == 1:
                # Add 1 because bounds are inclusive. Subtract if a zero is in there
                answer = max(answer, i - left + 1 - zero_included)
                continue

            if num == 0:
                zero_included = 1
                # Move the left bound to the right of the last zero
                left = last_zero + 1
                last_zero = i

        # If we never see a zero we must delete a num anyways
        if zero_included == 0:
            answer -= 1

        return answer

test_cases = [
    [3, [1,1,0,1]],
    [5, [0,1,1,1,0,1,1,0,1]],
    [2, [1,1,1]],
    [1, [1,0,0,0,0]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.longestSubarray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")