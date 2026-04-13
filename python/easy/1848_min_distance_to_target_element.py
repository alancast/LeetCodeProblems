class Solution:
    # Start at target and go both directions til answer is found
    # Time O(n)
    # Space O(1)
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        n = len(nums)

        for i in range(n):
            if start + i < n and nums[start + i] == target:
                return i
            if start - i >= 0 and nums[start - i] == target:
                return i

        # This will never happen could throw here
        return 0

test_cases = [
    [1, [1,2,3,4,5], 5, 3],
    [0, [1], 1, 0],
    [0, [1,1,1,1,1,1,1,1,1,1], 1, 0]
]
solution = Solution()
for expected, nums, target, start in test_cases:
    actual = solution.getMinDistance(nums, target, start)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, target: {target}, start: {start}")

print("Ran all tests")
