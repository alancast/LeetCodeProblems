class Solution:
    # Time O(n) as we go through nums array once
    # Space O(n) as we keep a set which could be the size of the full array
    def divideArray(self, nums: list[int]) -> bool:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                nums_set.add(num)

        return len(nums_set) == 0

test_cases = [
    [True, [3,2,3,2,2,2]],
    [False, [1,2,3,4]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.divideArray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
