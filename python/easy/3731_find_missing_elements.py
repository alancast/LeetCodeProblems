class Solution:
    # Find min and max in first pass, then see what's missing in second pass
    # Can also obviously sort in nlogn time
    # Time O(n)
    # Space O(max-min)
    def findMissingElements(self, nums: list[int]) -> list[int]:
        # Find min and max
        min_value = 99999999
        max_value = -99999999
        for num in nums:
            min_value = min(min_value, num)
            max_value = max(max_value, num)

        # Initialize an array of what is seen and what isn't
        seen = set(nums)

        # Go over range and see what's missing
        answer = []
        for value in range(min_value, max_value + 1):
            if value not in seen:
                answer.append(value)

        return answer

test_cases = [
    [[3], [1,4,2,5]],
    [[], [7,8,6,9]],
    [[2,3,4], [5,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.findMissingElements(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
