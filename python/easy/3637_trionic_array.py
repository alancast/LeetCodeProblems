from typing import List


class Solution:
    # Just go over array and see if it changes direction
    # Time O(n)
    # Space O(1)
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        increase_one = decrease_one = increase_two = False

        prev_num = nums[0]
        for i in range(1, n):
            num = nums[i]
            if num == prev_num:
                return False

            # Before first phase
            if not increase_one:
                if num <= prev_num:
                    return False

                increase_one = True
            # In first phase
            elif increase_one and not decrease_one:
                if num < prev_num:
                    decrease_one = True
            # In second phase
            elif decrease_one and not increase_two:
                if num > prev_num:
                    increase_two = True
            # In third phase (must always be greater)
            elif increase_two:
                if num <= prev_num:
                    return False

            prev_num = num

        return increase_two

test_cases = [
    [True, [1,3,5,4,2,6]],
    [False, [2,1,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.isTrionic(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
