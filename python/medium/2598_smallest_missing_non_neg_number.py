from typing import List


class Solution:
    # Go over all nums and see what they are mod value
    # Smallest remaining mod value is smallest number that can't be gotten
    # Time O(n)
    # Space O(value)
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = [0] * value
        for num in nums:
            mods[num%value] += 1
        
        # Find mod that will get used up first
        stopping_index = mods.index(min(mods))
        return (mods[stopping_index] * value) + stopping_index

test_cases = [
    [4, [1,-10,7,13,6,8], 5],
    [2, [1,-10,7,13,6,8], 7],
    [10 ,[3,0,3,2,4,2,1,1,0,4], 5]
]
solution = Solution()
for expected, nums, value in test_cases:
    actual = solution.findSmallestInteger(nums, value)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, value: {value}")

print("Ran all tests")