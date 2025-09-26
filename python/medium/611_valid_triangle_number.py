from typing import List


class Solution:
    # Sort nums, then iterate backwards and find right and left bound for pairs
    # Time O(n^2)
    # Space O(n) for sort
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        answer = 0

        for i in range(n - 1, -1, -1):
            left = 0
            right = i - 1
            num_i = nums[i]

            # Find left and right bounds
            while left < right:
                # This range everything in it is valid
                if nums[left] + nums[right] > num_i:
                    answer += right - left
                    right -= 1
                else:
                    left += 1

        return answer

    # Sort nums, then go over all i,j pairs and find right bound of k pair
    # Time O(n^2)
    # Space O(n) for sort
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        answer = 0

        k = n - 1
        # Go over all first nums
        for i in range(n-2):
            num_1 = nums[i]
            # Make sure we don't have a pair with a value of zero
            if num_1 == 0:
                continue

            k = i + 2
            # Go over all second nums in pair
            for j in range(i+1, n-1):
                num_2 = nums[j]

                # Find the right bound of k pairs
                while k < n and num_1 + num_2 > nums[k]:
                    k += 1

                # Add all the pairs
                answer += k - j - 1

        return answer

test_cases = [
    [3, [2,2,3,4]],
    [4, [4,2,3,4]],
    [0, [7,0,0,0]],
    [0, [0,1,0,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.triangleNumber(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")