class Solution:
    # Go over array once and count how many numbers less than
    # Time O(n)
    # Space O(1)
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count_smaller = 0
        count_equal = 0

        # Go over every num in array and count how many smaller and equal
        for num in nums:
            if num < target:
                count_smaller += 1
            elif num == target:
                count_equal += 1

        # Create the answer array of indices
        return list(range(count_smaller, count_smaller + count_equal))

test_cases = [
    [[1,2], [1,2,5,2,3], 2],
    [[3], [1,2,5,2,3], 3],
    [[4], [1,2,5,2,3], 5]
]
solution = Solution()
for expected, nums, target in test_cases:
    actual = solution.targetIndices(nums, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, target: {target}")

print("Ran all tests")

