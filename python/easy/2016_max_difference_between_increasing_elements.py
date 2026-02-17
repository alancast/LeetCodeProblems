class Solution:
    # Time O(n) as we go through the list once
    # Space O(1)
    def maximumDifference(self, nums: list[int]) -> int:
        max_diff = -1

        lowest = float('inf')
        for num in nums:
            if num <= lowest:
                lowest = num
                continue

            max_diff = max(max_diff, num - lowest)

        return int(max_diff)

test_cases = [
    [4, [7,1,5,4]],
    [-1, [9,4,3,2]],
    [9, [1,5,2,10]],
    [-1, [1,1,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maximumDifference(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
