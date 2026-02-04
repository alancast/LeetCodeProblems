from typing import List


class Solution:
    # Go over array and find strictly decreasing part
    # Then go to left and right to find increase and see if it creates a max
    # Time O(n)
    # Space O(1)
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        answer = float('-inf')

        # Go over array finding decreasing parts to test ends on
        i = 1
        while i < n - 2:
            inc_one_start = dec_end = i
            dec_sum = nums[inc_one_start]

            # Find strictly decreasing subarray starting at i
            while dec_end + 1 < n and nums[dec_end + 1] < nums[dec_end]:
                dec_sum += nums[dec_end + 1]
                dec_end += 1
            # No strictly decreasing starting at this i, so increment i
            if dec_end == inc_one_start:
                i += 1
                continue

            # Find increasing array to left of start of decreasing
            left_sum = 0
            left_max_sum = float('-inf')
            while inc_one_start - 1 >= 0 and nums[inc_one_start - 1] < nums[inc_one_start]:
                left_sum += nums[inc_one_start - 1]
                # We don't necessarily just take sum, as nums could be negative
                left_max_sum = max(left_max_sum, left_sum)
                inc_one_start -= 1
            # No strictly increasing array to left of i, so increment i
            if inc_one_start == i:
                i += 1
                continue

            # Find increasing array to right of end of decreasing
            inc_two_end = dec_end
            right_sum = 0
            right_max_sum = float('-inf')
            while dec_end + 1 < n and nums[dec_end + 1] > nums[dec_end]:
                right_sum += nums[dec_end + 1]
                # We don't necessarily just take sum, as nums could be negative
                right_max_sum = max(right_max_sum, right_sum)
                dec_end += 1
            # No strictly increasing array to right of i, so increment i
            if dec_end == inc_two_end:
                i += 1
                continue

            # Found a possible answer, so see if it works then move forward i
            answer = max(answer, left_max_sum + right_max_sum + dec_sum)
            i = inc_two_end

        # If no Trionic array was found
        if answer == float('-inf'):
            return 0

        return int(answer)

test_cases = [
    [-4, [0,-2,-1,-3,0,2,-1]],
    [14, [1,4,2,7]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxSumTrionic(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
