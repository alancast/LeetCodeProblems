class Solution:
    # Go over array once and find min and max indexes then see what is best for removal
    # Time O(n)
    # Space O(1)
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        min_index = max_index = -1
        min_value = 99999999
        max_value = -99999999

        # Go over array once and find min and max
        for i in range(n):
            num = nums[i]
            if num < min_value:
                min_value = num
                min_index = i
            if num > max_value:
                max_value = num
                max_index = i

        # Delete both from left
        left_deletions = max(min_index, max_index) + 1
        # Delete both from right
        right_deletions = n - min(min_index, max_index)

        # Delete one from left and one from right
        mixed_deletions = min((min_index + 1), (max_index + 1)) + min((n - min_index), (n - max_index))

        return min(left_deletions, right_deletions, mixed_deletions)

test_cases = [
    [2, [1000,10,7,5,4,1,8,6,-1000]],
    [5, [2,10,7,5,4,1,8,6]],
    [3, [0,-4,19,1,8,-2,-3,5]],
    [1, [101]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumDeletions(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
