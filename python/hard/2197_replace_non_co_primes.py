from math import gcd
from typing import List


class Solution:
    # Time O(nlogc)
    # Space O(1)
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        answer = []

        # Go over all nums perform the replacement operation until nums[i]
        # And the element at the top are coprime, or stack becomes empty.
        for num in nums:
            while answer:
                g = gcd(answer[-1], num)
                if g > 1:
                    num = answer[-1] // g * num
                    answer.pop()
                else:
                    break
            answer.append(num)

        return answer

test_cases = [
    [[12,7,6], [6,4,3,2,7,6,2]],
    [[2,1,1,3], [2,2,1,1,3,3,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.replaceNonCoprimes(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")