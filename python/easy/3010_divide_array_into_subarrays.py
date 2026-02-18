class Solution:
    # Just go over array once and find two lowest numbers other than first
    # Time O(n)
    # Space O(1)
    def minimumCost(self, nums: list[int]) -> int:
        lowest = second_lowest = float('inf')

        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            if num <= lowest:
                second_lowest = lowest
                lowest = num
            elif num < second_lowest:
                second_lowest = num

        return int(nums[0] + lowest + second_lowest)

test_cases = [
    [6, [1,2,3,12]],
    [12, [5,4,3]],
    [12, [10,3,1,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumCost(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
