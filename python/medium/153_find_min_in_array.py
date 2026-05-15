class Solution:
    # Binary search variant where you see if left is greater than right or not
    # Time O(logn)
    # Space O(1)
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        # If the last num is greater than first num there is no rotation so min is first
        if nums[right] > nums[0]:
            return nums[0]

        # Do the binary search
        while left < right:
            # To avoid potential overflow
            mid = left + ((right - left) // 2)

            # End condition (means left and right are off by 1)
            if mid == left:
                return min(nums[left], nums[right])

            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid

        # This will never happen as we always return from within the loop
        return nums[left]

test_cases = [
    [1, [3,4,5,1,2]],
    [1, [3,4,5,1]],
    [0, [4,5,6,7,0,1,2]],
    [11, [11,13,15,17]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.findMin(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
