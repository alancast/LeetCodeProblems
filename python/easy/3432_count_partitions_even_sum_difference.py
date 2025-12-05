from typing import List


class Solution:
    # Can do with math. If sum is odd no partitions work
    # If sum is even all partitions work
    # Time O(n)
    # Space O(1)
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        if total_sum % 2 == 0:
            return len(nums) - 1
        else:
            return 0

    # Go over array once to find sum
    # Go over second time and compute running sum and see if partition works
    # Time O(n)
    # Space O(1)
    def countPartitions_compute(self, nums: List[int]) -> int:
        n = len(nums)
        right_sum = sum(nums)

        answer = 0
        left_sum = 0
        # Go over nums and compute running left and right sum
        # Don't include final number
        for i in range(n-1):
            num = nums[i]
            left_sum += num
            right_sum -= num
            if (right_sum - left_sum) % 2 == 0:
                answer += 1

        return answer

test_cases = [
    [4, [10,10,3,7,6]],
    [0, [1,2,2]],
    [3, [2,4,6,8]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.countPartitions(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")