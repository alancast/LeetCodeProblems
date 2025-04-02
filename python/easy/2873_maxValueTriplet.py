from typing import List

class Solution:
    # Time O(n) space O(1)
    # Iterate through keeping track of stats and compute each time
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = max_num = max_difference = 0
        for num in nums:
            # Compute product with this number
            answer = max(answer, (max_difference * num))

            # See if future product could be bettered by including it
            max_difference = max(max_difference, (max_num - num))
            max_num = max(max_num, num)

        return answer
    
solution = Solution()
test_cases = [
    [273, [15,2,18,20,21]],
    [399, [15,2,18,20,1,21]],
    [260, [15,2,18,7,20]],
    [260, [15,2,18,20]],
    [77, [12,6,1,2,7]],
    [0, [1,2,3]],
    [0, [1,1,1]],
    [1, [3,2,1]],
    [133, [1,10,3,4,19]]
]
for expected, nums in test_cases:
    answer = solution.maximumTripletValue(nums)
    if answer != expected:
        print(f"FAILED TEST! Expected {expected} but got {answer}. INPUTS: nums: {nums}")

print("Ran all tests!")