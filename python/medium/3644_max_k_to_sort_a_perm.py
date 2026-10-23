class Solution:
    # Just go over once and compute bitwise AND
    # Time O(n)
    # Space O(1)
    def sortPermutation(self, nums: list[int]) -> int:
        n = len(nums)

        # Go over all nums and bitwise AND all relevant ones
        answer = -1
        for i in range(n):
            # Skip if num equals the index
            if nums[i] == i:
                continue

            # Update running bitwise AND
            answer &= nums[i]

        return 0 if answer == -1 else answer

test_cases = [
    [1, [0,3,2,1]],
    [2, [0,1,3,2]],
    [0, [3,2,1,0]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.sortPermutation(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
