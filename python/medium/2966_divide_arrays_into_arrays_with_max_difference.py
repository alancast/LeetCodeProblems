from typing import List


class Solution:
    # Sort array then just parse out into smaller subarrays
    # If any difference is greater than k not possible
    # Time O(nlogn)
    # Space O(n) for sorting algorithm
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        # This is the time killer in here
        nums.sort()

        answer = []
        # Go through full array and split it into groups of 3 and make sure they all work
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []

            answer.append([nums[i], nums[i + 1], nums[i + 2]])

        return answer

test_cases = [
    [[[1,1,3],[3,4,5],[7,8,9]], [1,3,4,8,7,9,3,5,1], 2],
    [[], [2,4,2,2,5,2], 2]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.divideArray(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")