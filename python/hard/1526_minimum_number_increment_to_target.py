from typing import List


class Solution:
    # Go over length of array and see how many needed individually for each number
    # Can take advantage of incrementing past ones with it
    # Time O(n)
    # Space O(1)
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        answer = target[0]
        prev = target[0]

        # Go over whole array
        for i in range(1, n):
            # Do we need to increment this separate from previous one or no?
            if target[i] >= prev:
                answer += target[i] - prev
        
            prev = target[i]

        return answer

test_cases = [
    [3, [1,2,3,2,1]],
    [4, [3,1,1,2]],
    [7, [3,1,5,4,2]]
]
solution = Solution()
for expected, target in test_cases:
    actual = solution.minNumberOperations(target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: target: {target}")

print("Ran all tests")