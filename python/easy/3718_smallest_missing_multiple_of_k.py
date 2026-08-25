class Solution:
    # Create a set of the list and then just multiply k
    # Time O(n)
    # Space O(n)
    def missingMultiple(self, nums: list[int], k: int) -> int:
        nums_set = set(nums)

        i = 1
        while i*k in nums_set:
            i += 1

        return i*k

test_cases = [
    [10, [8,2,3,4,6], 2],
    [5, [1,4,7,10,15], 5]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.missingMultiple(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
