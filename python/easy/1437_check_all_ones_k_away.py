from typing import List


class Solution:
    # Go over array and just keep track of index of 1s
    # Time O(n)
    # Space O(1)
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_index = -1
        for i, num in enumerate(nums):
            # If this number is a one check if it's too close
            if num == 1:
                if last_one_index > -1 and last_one_index + k >= i:
                    return False
                
                last_one_index = i

        # Got through whole array and none are too close
        return True

test_cases = [
    [True, [1,0,0,0,1,0,0,1], 2],
    [False, [1,0,0,1,0,1], 2]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.kLengthApart(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")