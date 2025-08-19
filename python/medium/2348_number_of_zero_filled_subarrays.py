from typing import List


class Solution:
    # Go over array once and count consecutive 0's and do math
    # Time O(n)
    # Space O(1)
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        count = 0

        # Add 0's in duration of array
        for num in nums:
            if num == 0:
                count += 1
                continue

            # Got a non-zero, so add how many subarrays to answer and reset
            answer += (count * (count + 1))//2
            count = 0

        # Add final amount if nums ended with a 0
        answer += (count * (count + 1))//2

        return answer

test_cases = [
    [6, [1,3,0,0,2,0,0,4]],
    [9, [0,0,0,2,0,0]],
    [0, [2,10,2019]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.zeroFilledSubarray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")