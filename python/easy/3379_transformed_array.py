from typing import List


class Solution:
    # Go over array once and find proper value for each entry
    # Time O(n)
    # Space O(1)
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = []

        for i in range(n):
            num = nums[i]
            if num != 0:
                answer.append(nums[(num + i) % n])
            else:
                answer.append(num)

        return answer

test_cases = [
    [[1,1,1,3], [3,-2,1,1]],
    [[-1,-1,4], [-1,4,-1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.constructTransformedArray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
