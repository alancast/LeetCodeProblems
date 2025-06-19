from typing import List


class Solution:
    # Sort then just go through and count
    # Time O(nlogn) for sorting
    # Space O(n) for sort algo
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        answer = 1
        lower_bound = nums[0]
        for num in nums:
            if num - lower_bound > k:
                answer += 1
                lower_bound = num

        return answer
    
test_cases = [
    [2, [3,6,1,2,5], 2],
    [2, [1,2,3], 1],
    [3, [2,2,4,5], 0]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.partitionArray(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")