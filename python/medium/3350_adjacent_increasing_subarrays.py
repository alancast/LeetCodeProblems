from typing import List


class Solution:
    # Go over array once and count counts and previous counts
    # Time O(n)
    # Space O(1)
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        count = previous_count = answer = 0
        prev_num = float('-inf')

        for num in nums:
            if num > prev_num:
                count += 1
                answer = max(answer, count//2)
            else:
                answer = max(answer, min(count, previous_count))
                previous_count = count
                count = 1
            
            prev_num = num

        # See if final one is best answer
        answer = max(answer, min(count, previous_count))

        return answer

test_cases = [
    [3, [2,5,7,8,9,2,3,4,3,1]],
    [1, [19,5]],
    [2, [1,2,3,4,4,4,4,5,6,7]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxIncreasingSubarrays(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
