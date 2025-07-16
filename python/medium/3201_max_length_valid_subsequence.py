from typing import List


class Solution:
    # Time O(n) as we go over the array once
    # Space O(1)
    def maximumLength(self, nums: List[int]) -> int:
        odds = evens = 0 
        alternating = 1 # because first one isn't counted
        previous_even = nums[0] % 2 == 0

        for num in nums:
            if num % 2 == 1:
                odds += 1
                if previous_even:
                    previous_even = False
                    alternating += 1
            else:
                evens += 1
                if not previous_even:
                    previous_even = True
                    alternating += 1

        return max(odds, evens, alternating)
    
test_cases = [
    [4, [1,2,3,4]],
    [6, [1,2,1,1,2,1,2]],
    [2, [1,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maximumLength(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")