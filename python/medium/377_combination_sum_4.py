from typing import List


class Solution:
    # Bottom up dynamic programming. How many ways to make number from 0 to target
    # Time O(t * n) where t is target and n is len nums
    # Space O(t)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combinations = [0] * (target + 1)
        combinations[0] = 1

        # Compute ways to build each number
        for i in range(target + 1):
            # Add all combinations that add each part of num
            for num in nums:
                if i - num < 0:
                    continue

                combinations[i] += combinations[i-num]

        return combinations[target]
    
test_cases = [
    [7 , [1,2,3], 4],
    [0, [9], 3]
]
solution = Solution()
for expected, nums, target in test_cases:
    actual = solution.combinationSum4(nums, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}, target: {target}")

print("Ran all tests")