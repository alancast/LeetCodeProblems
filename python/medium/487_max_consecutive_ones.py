from typing import List


class Solution:
    # Time O(n) as we just go through nums once
    # Space O(1) as we just keep a couple variables
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = current_count = backup_count = 0
        current_flipped = False

        for num in nums:
            if num == 1:
                current_count += 1
                backup_count += 1
                continue

            else:
                if current_flipped:
                    max_count = max(current_count, max_count)
                    current_count = backup_count + 1
                    backup_count = 0
                    continue

                else:
                    current_flipped = True
                    current_count += 1
                    backup_count = 0


        return max(max_count, current_count)
    
test_cases = [
    [4, [1,0,1,1,0]],
    [4, [1,0,1,1,0,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.findMaxConsecutiveOnes(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")