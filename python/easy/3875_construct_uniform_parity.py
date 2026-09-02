class Solution:
    # It's always possible. Because either nums1 is all odd or all even, easy
    # Or nums1 has some odd and even, so just subtract and make all odd
    # Time O(1)
    # Space O(1)
    def uniformArray(self, nums1: list[int]) -> bool:
        return True

test_cases = [
    [True, [2,3]],
    [True, [4,6]]
]
solution = Solution()
for expected, nums1 in test_cases:
    actual = solution.uniformArray(nums1)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums1: {nums1}")

print("Ran all tests")
