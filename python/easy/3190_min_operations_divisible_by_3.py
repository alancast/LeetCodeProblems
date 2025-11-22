from typing import List


class Solution:
    # For every num if it isn't already mod 3 you can always add or subtract 1 to make it so
    # So just go over list once and count how many aren't mod 3
    # Time O(n)
    # Space O(1)
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            if num % 3 != 0:
                answer += 1

        return answer

test_cases = [
    [3, [1,2,3,4]],
    [0, [3,6,9]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumOperations(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")