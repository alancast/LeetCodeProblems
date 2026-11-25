from math import gcd


class Solution:
    # Any two numbers form a product equivalent subarray
    # For longer subarrays, the numbers need to be pairwise coprime
    # Keep a sliding window of pairwise coprime numbers
    # Time O(n)
    # Space O(1)
    def maxLength(self, nums: list[int]) -> int:
        answer = 2
        current_product = 1
        left = 0

        # Shrink the window until the next number is coprime with the product
        for right, num in enumerate(nums):
            while gcd(current_product, num) > 1:
                current_product //= nums[left]
                left += 1

            current_product *= num
            answer = max(answer, right - left + 1)

        return answer


test_cases = [
    [5, [1, 2, 1, 2, 1, 1, 1]],
    [3, [2, 3, 4, 5, 6]],
    [5, [1, 2, 3, 1, 4, 5, 1]],
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxLength(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}")

print("Ran all tests")
