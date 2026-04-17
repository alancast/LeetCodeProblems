class Solution:
    # Go over nums once and tore mirrors when we see a number
    # Time O(n)
    # Space O(n)
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        answer = n = len(nums)
        # Dictionary of numbers mirror to the last time it showed up
        mirrors = {}

        for i, num in enumerate(nums):
            if num in mirrors:
                answer = min(answer, i - mirrors[num])

            mirrors[int(str(num)[::-1])] = i

        # See if we found a pair or not
        return -1 if answer == n else answer

test_cases = [
    [1, [12,21,45,33,54]],
    [1, [120,21]],
    [-1, [21,120]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minMirrorPairDistance(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
