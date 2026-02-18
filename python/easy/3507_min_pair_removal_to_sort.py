class Solution:
    # Go over whole array every time until sorted
    # Can keep a second array next_index which points to next index
    # This would make deletion O(1) but make space O(n)
    # Time O(n^2)
    # Space O(1)
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        pairs_removed = 0

        sorted = False
        # Keep doing operation until sorted
        while not sorted:
            sorted = True
            min_sum_index = 0
            min_sum = float('inf')

            # Go over array to find min sum and see if sorted
            for i in range(1, n - pairs_removed):
                if nums[i-1] > nums[i]:
                    sorted = False

                if nums[i-1] + nums[i] < min_sum:
                    min_sum_index = i-1
                    min_sum = nums[i-1] + nums[i]

            # See if we need to remove a pair and then do it
            if not sorted:
                nums[min_sum_index] = nums[min_sum_index] + nums[min_sum_index + 1]
                nums.pop(min_sum_index + 1)
                pairs_removed += 1

        return pairs_removed

test_cases = [
    [2, [5,2,3,1]],
    [0, [1,2,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumPairRemoval(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
