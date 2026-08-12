from collections import defaultdict


class Solution:
    # Sliding window with counter
    # Time O(n)
    # Space O(n)
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        start = answer = 0
        counts = defaultdict(int)

        for end in range(n):
            num = nums[end]
            counts[num] += 1

            # See if we have too many and remove from front if we do
            while counts[num] > k:
                counts[nums[start]] -= 1
                start += 1

            answer = max(answer, end - start + 1)

        return answer

test_cases = [
    [6, [1,2,3,1,2,3,1,2], 2],
    [2, [1,2,1,2,1,2,1,2], 1],
    [4, [5,5,5,5,5,5,5], 4]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.maxSubarrayLength(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
