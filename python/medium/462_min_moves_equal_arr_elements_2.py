class Solution:
    # Sort and find midpoint
    # Time O(nlogn)
    # Space O(n) for sort
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        nums.sort()

        mid = nums[n//2]

        answer = 0
        for i in nums:
            answer += abs(i - mid)

        return answer

test_cases = [
    [2, [1,2,3]],
    [16, [1,10,2,9]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minMoves2(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
