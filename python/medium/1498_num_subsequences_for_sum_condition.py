import bisect
from typing import List


class Solution:
    # Similar logic to below but no need for binary search
    # Can sort and then just use a pointer to right and left
    # Time O(nlogn) for sorting algorithm
    # Space O(n) for sorting algorithm
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7

        n = len(nums)
        nums.sort()

        answer = left = 0
        right = n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                answer += pow(2, right - left, mod) % mod
                left += 1
            else:
                right -= 1

        return answer % mod
    
    # Time O(nlogn) for sorting algorithm as well as binary searches
    # Space O(n) for sorting algorithm
    def numSubseq_binary_search(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7

        n = len(nums)
        nums.sort()

        answer = 0

        # every starting min find how many nums we need to exclude
        for i in range(n):
            min_num = nums[i]
            max_possible = target - min_num

            # We can no longer create a subset that isn't already counted
            if max_possible < min_num:
                break

            # Find rightmost index (largest num) still useable and compute subsequences
            right = bisect.bisect_right(nums, max_possible) - 1
            answer += pow(2, right - i, mod)


        return answer % mod
    
test_cases = [
    [4, [3,5,6,7], 9],
    [6, [3,3,6,8], 10],
    [61, [2,3,3,4,6,7], 12],
    [272187084, [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14], 22]
]
solution = Solution()
for expected, nums, target in test_cases:
    actual = solution.numSubseq(nums, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, target: {target}")

print("Ran all tests")