from typing import List


class Solution:
    # Sort array and then go over all nums and see how far right we can go
    # Time O(nlogn + n)
    # Space O(n) for sorting
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        # Upper bound is remove everything
        answer = n

        # See how far right you can go for a given num
        right = 0
        for left in range(n):
            # How far right can we go with this left num
            while right < n and nums[right] <= nums[left] * k:
                right += 1

            # See if this is a new answer min
            answer = min(answer, n - (right - left))

        return answer

test_cases = [
    [1, [2,1,5], 2],
    [2, [1,6,2,9], 3],
    [0, [4,6], 2]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.minRemoval(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
