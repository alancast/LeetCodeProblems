class Solution:
    # One pass solution
    # Time O(n)
    # Space O(1)
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        # Track current lengths of increasing and decreasing sequences
        inc_length = dec_length = max_length = 1

        # Iterate through array comparing adjacent elements
        for pos in range(len(nums) - 1):
            if nums[pos + 1] > nums[pos]:
                # If next element is larger, extend increasing sequence
                inc_length += 1
                dec_length = 1  # Reset decreasing sequence
            elif nums[pos + 1] < nums[pos]:
                # If next element is smaller, extend decreasing sequence
                dec_length += 1
                inc_length = 1  # Reset increasing sequence
            else:
                # If elements are equal, reset both sequences
                inc_length = dec_length = 1

            # Update max length considering both sequences
            max_length = max(max_length, inc_length, dec_length)

        return max_length

test_cases = [
    [2, [1, 4, 3, 3, 2]],
    [1, [3, 3, 3, 3]],
    [3, [3, 2, 1]],
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.longestMonotonicSubarray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}")

print("Ran all tests")
