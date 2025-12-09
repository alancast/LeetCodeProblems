from collections import Counter, defaultdict
from typing import List


class Solution:
    MOD = 10**9 + 7

    # Go over nums once to create counter of nums
    # Go over again and decrement count left to right
    # While incrementing count to left. Use counts to find pairs
    # Time O(n)
    # Space O(n)
    def specialTriplets(self, nums: List[int]) -> int:
        right_side_counts = Counter(nums)

        answer = 0

        # Go from left to right and find out how many left side counts
        # Decrement right side as you go
        left_side_counts = defaultdict(int)
        for num in nums:
            # Decrement right side as no longer to right
            right_side_counts[num] -= 1

            # Find out how many *2 there are and add pairs
            answer += (left_side_counts[num*2] * right_side_counts[num*2])
            answer %= self.MOD

            # Increment left side as one to left now
            # Done after answer addition because of 0 corner case
            left_side_counts[num] += 1

        return answer

test_cases = [
    [1, [6,3,6]],
    [2, [6,3,6,6]],
    [4, [6,6,3,6,6]],
    [1, [0,1,0,0]],
    [2, [8,4,2,8,4]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.specialTriplets(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")