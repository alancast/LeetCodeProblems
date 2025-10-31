from typing import List


class Solution:
    # Create a set, go through each num, if it's already in set add to answer
    # Can also sort and take O(1) space but O(nlogn) time
    # Time O(n)
    # Space O(n)
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_set = set()
        answer = []
        for num in nums:
            if num in num_set:
                answer.append(num)
            
            num_set.add(num)

        return answer

test_cases = [
    [[1,0], [0,1,1,0]],
    [[3,2], [0,3,2,1,3,2]],
    [[4,5], [7,1,5,4,3,4,6,0,9,5,8,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.getSneakyNumbers(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")