from typing import List
from bisect import bisect_left


class Solution:
    # Sort the array and then use two pointers
    # Time O(n^2)
    # Space O(n) for sort
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()


        answer = 0
        for i in range(n - 2):
            num_i = nums[i]

            # Now do 2 sum smaller which is O(n) but with num_i locked
            l = i+1
            r = n-1
            while l < r:
                triplet_sum = num_i + nums[l] + nums[r]

                # If triplet sum works, make lower bound (l) larger
                if triplet_sum < target:
                    # All pairs this and in between work
                    answer += r - l
                    l += 1
                # If it's too big, make upper bound (r) smaller
                else:
                    r -= 1
            
        return answer

    # Sort the array and then binary search to find ending num
    # Time O(nlogn + n^2logn)
    # Space O(n) for sort
    def threeSumSmaller_binary_search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        # Fix all first 2 pairs and then find how many 3rd are left
        answer = 0
        for i in range(n-2):
            num_i = nums[i]
            for j in range(i+1, n-1):
                num_j = nums[j]
                pair_sum = num_i + num_j
                max_left = target - pair_sum
                right_idx = bisect_left(nums, max_left, j+1)
                answer += max(0, right_idx - (j+1))

        return answer

test_cases = [
    [2, [-2,0,1,3], 2],
    [1, [-1,1,-1,-1], -1],
    [0, [], 0],
    [0, [0], 0]
]
solution = Solution()
for expected, nums, target in test_cases:
    actual = solution.threeSumSmaller(nums, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, target: {target}")

print("Ran all tests")