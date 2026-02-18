class Solution:
    # All you need is the sum of the array and mod k and how much it's off by
    # Time O(n)
    # Space O(1)
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k

test_cases = [
    [4, [3,9,7], 5],
    [0, [4,1,3], 4],
    [5, [3,2], 6]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.minOperations(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
