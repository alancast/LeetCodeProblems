from typing import List


class Solution:
    # Sliding window and bitwise or
    # Time O(n) as we go through nums at most twice
    # Space O(1)
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = longest = 1
        ored_num = nums[left]

        while right < n:
            right_num = nums[right]
            if right_num & ored_num == 0:
                ored_num = ored_num | right_num
                longest = max(longest, right - left + 1)
            # The streak is broken so move left forward until it's not
            else:
                while ored_num & right_num != 0:
                    left_num = nums[left]
                    ored_num = ored_num & ~left_num
                    left += 1
                
                ored_num = ored_num | right_num

            right += 1

        return longest

    # Time O(n^2) as we see how long we can make from every i
    # Space O(1)
    def longestNiceSubarray_brute_force(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 1

        for i, num in enumerate(nums):
            ored_num = num
            streak = 1
            for j in range(i+1, n):
                j_num = nums[j]
                if ored_num & j_num != 0:
                    break

                ored_num = ored_num | j_num
                streak += 1

            longest = max(longest,streak)

        return longest
    
test_cases = [
    [3, [1,3,8,48,10]],
    [4, [1,3,8,48,1,4]],
    [1, [3,1,5,11,13]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.longestNiceSubarray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")