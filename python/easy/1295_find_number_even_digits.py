class Solution:
    # Time O(n) as just go through numbers once
    # Space O(1)
    # Bounds of problem say all numbers <= 100k so just number check
    # If bounds weren't known could convert to string and do string len
    # Or divide by 10 until equals zero and count num times
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for num in nums:
            if (
                (num >= 10 and num < 100)  # noqa: PLR2004
                or (num >= 1000 and num < 10000)  # noqa: PLR2004
                or num == 100000  # noqa: PLR2004
            ):
                count += 1

        return count

test_cases = [
    [1, [555, 901, 482, 1771]],
    [2, [12, 345, 2, 6, 7896]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.findNumbers(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
