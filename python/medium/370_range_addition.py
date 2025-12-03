from typing import List


class Solution:
    # Build array with prefix sum
    # Time O(U + n)
    # Space O(1) all we need is answer array
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Initialize array with 1 extra to account for things that end at end
        answer = [0] * (length + 1)

        # Update start and end ranges
        for start, end, val in updates:
            answer[start] += val
            answer[end + 1] -= val

        # Go over answer array and update values
        prefix_sum = 0
        for i in range(length):
            prefix_sum += answer[i]
            answer[i] = prefix_sum

        # Remove last item that's no longer needed
        answer.pop()
        return answer

test_cases = [
    [[-2,0,3,5,3], 5, [[1,3,2],[2,4,3],[0,2,-2]]],
    [[0,-4,2,2,2,4,4,-4,-4,-4], 10, [[2,4,6],[5,6,8],[1,9,-4]]]
]
solution = Solution()
for expected, length, updates in test_cases:
    actual = solution.getModifiedArray(length, updates)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: length: {length}, updates: {updates}")

print("Ran all tests")