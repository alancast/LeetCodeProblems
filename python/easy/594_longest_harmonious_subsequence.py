from collections import Counter, defaultdict


class Solution:
    # Same logic as counter but one pass
    # Hash map for counts and each time we get a num see it's neighbors
    # Time O(n) as we just go over array once
    # Space O(n) for storing counts
    def findLHS(self, nums: list[int]) -> int:
        num_counts = defaultdict(int)
        answer = 0

        for num in nums:
            # Count num
            num_counts[num] += 1

            # Check neighbors
            if num_counts[num-1] > 0:
                answer = max(answer, num_counts[num] + num_counts[num - 1])
            if num_counts[num+1] > 0:
                answer = max(answer, num_counts[num] + num_counts[num + 1])

        return answer

    # Hash map then loop over keys
    # Time O(n) as we just go over array at most twice
    # Space O(n) for storing counts
    def findLHS_counter(self, nums: list[int]) -> int:
        num_counts = Counter(nums)
        answer = 0

        for num in num_counts:
            # Check neighbors but only need to check in one direction
            # as it'll be caught by one neighbor
            if num - 1 in num_counts:
                answer = max(answer, num_counts[num] + num_counts[num - 1])

        return answer

    # Sort array, then have sliding window and get max sliding window size
    # Time O(nlogn) for sort
    # Space O(n) for sort
    def findLHS_sorting(self, nums: list[int]) -> int:
        nums.sort()

        left = answer = 0
        for right, num in enumerate(nums):
            # If they numbers are the same it's not harmonious
            if num == nums[left]:
                continue

            # If left gets too small move it forward
            while left < right and nums[left] < num - 1:
                left += 1

            # No number 1 smaller than current
            if left == right:
                continue

            answer = max(answer, right - left + 1)

        return answer

test_cases = [
    [5, [1,3,2,2,5,2,3,7]],
    [2, [1,2,3,4]],
    [0, [1,3,5,7]],
    [0, [1,1,1,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.findLHS(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
