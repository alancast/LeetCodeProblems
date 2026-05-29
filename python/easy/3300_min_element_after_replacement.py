class Solution:
    # Just go over list and sum nums and store min
    # Time O(n)
    # Space O(1)
    def minElement(self, nums: list[int]) -> int:
        # Start with just really high number (above problem bounds)
        answer = 99999999

        for num in nums:
            dig_sum = 0
            while num > 0:
                dig_sum += num % 10
                num //= 10  # noqa: PLW2901

            answer = min(dig_sum, answer)

        return answer

test_cases = [
    [1, [10,12,13,14]],
    [1, [1,2,3,4]],
    [10, [999,19,199]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minElement(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
