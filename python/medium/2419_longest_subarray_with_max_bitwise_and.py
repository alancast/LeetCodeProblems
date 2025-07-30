from typing import List


class Solution:
    # Time O(n) as we go through the whole array once
    # Space O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        answer = count = 0
        last_num = max_num = -1

        for num in nums:
            if num != last_num:
                count = 1
            else:
                count += 1

            # If we have a new max_num
            if num > max_num:
                max_num = num
                answer = count
            # Longer streak of same max num
            elif num == max_num:
                answer = max(answer, count)
            
            last_num = num

        return answer
    
test_cases = [
    [2, [1,2,3,3,2,2]],
    [1, [1,2,3,4]],
    [1, [96317,96317,96317,96317,96317,96317,96317,96317,96317,279979]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.longestSubarray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")