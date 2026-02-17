class Solution:
    # Time O(n) Space O(1)
    def applyOperations(self, nums: list[int]) -> list[int]:
        num_index = 0
        # Do computations on everything in list
        for i in range(len(nums)-1):
            if nums[i] == 0:
                continue
            if nums[i] == nums[i+1]:
                nums[num_index] = nums[i] * 2
                nums[i+1] = 0
            else:
                nums[num_index] = nums[i]

            num_index += 1

        # Take care of last one as well
        nums[num_index] = nums[-1]
        num_index += 1

        # Make sure final entries are all 0's
        for i in range(num_index, len(nums)):
            nums[i] = 0

        return nums

test_cases = [
    [[1694,399,832,1758,412,206,272,0,0,0,0,0,0,0], [847,847,0,0,0,399,416,416,879,879,206,206,206,272]],
    [[1,4,2,0,0,0], [1,2,2,1,1,0]],
    [[1,0,0,0], [0,0,0,1]],
]
solution = Solution()
for expected, nums in test_cases:
    nums_copy = nums[:]
    actual = solution.applyOperations(nums_copy)
    if actual != expected:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests!")
