class Solution:
    # Compute all digit sums and just stop as soon as we find first one
    # Time O(nlogk) where k is max num
    # Space O(1)
    def smallestIndex(self, nums: list[int]) -> int:
        n = len(nums)

        # Go over all nums and see when digit sum equals index
        for i in range(n):
            num = nums[i]
            digit_sum = 0
            # Compute digit sum, break if we know it's not possible
            while digit_sum <= i and num > 0:
                digit_sum += num % 10
                num //= 10

            # See if this num is the answer
            if digit_sum == i:
                return i

        # None of the digit sums were right so return -1
        return -1

test_cases = [
    [2, [1,3,2]],
    [1, [1, 10, 11]],
    [-1, [1,2,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.smallestIndex(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
