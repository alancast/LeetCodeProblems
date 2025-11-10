from typing import List


class Solution:
    # Use a monotonic always increasing stack
    # Time O(n) as we go over all nums once
    # Space O(n)
    def minOperations(self, nums: List[int]) -> int:
        s = []
        answer = 0

        # Go over all nums in array
        for num in nums:
            # Make sure this num is greater than what's at the end of the stack
            while s and s[-1] > num:
                s.pop()
            
            # If this num is already 0 nothing to do
            if num == 0:
                continue
            # Add this to numbers to zero and add to stack
            if not s or s[-1] < num:
                answer += 1
                s.append(num)

        return answer

test_cases = [
    [1, [0,2]],
    [3, [3,1,2,1]],
    [4, [1,2,1,2,1,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minOperations(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")