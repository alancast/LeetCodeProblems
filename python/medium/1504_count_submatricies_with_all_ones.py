from typing import List


class Solution:
    # Monotonic stack where we see how tall columns of 1 are
    # Then go over those and find heights to left to see how many
    # Submatrices can end (bottom right) there
    # Time O(n*m) m is number of rows, n is cols
    # Space O(n) where n is number of columns
    def numSubmat(self, mat: List[List[int]]) -> int:
        cols = len(mat[0])
        heights = [0] * cols

        answer = 0
        for row in mat:
            # See how tall this stack of ones is in this column
            for i, x in enumerate(row):
                heights[i] = 0 if x == 0 else heights[i] + 1

            # Stack keeps track of [index, count, height]
            # This dummy entry with height -1 makes sure it's never popped
            # As smallest possible height is 0
            stack = [[-1, 0, -1]]
            # Go over all the height columns from left to right
            for i, h in enumerate(heights):
                # Pop from the stack until the top has a height
                # Smaller than this current column
                # Ensure stacks are strictly increasing in height
                while stack[-1][2] >= h:
                    stack.pop()

                # Get information from previously shorter column
                j, prev, _ = stack[-1]
                # Find how many submatricies end here
                cur = prev + (i - j) * h
                # Append new info to stack
                stack.append([i, cur, h])

                # Add submatricies ending here to count
                answer += cur

        return answer

test_cases = [
    [13, [[1,0,1],[1,1,0],[1,1,0]]],
    [24, [[0,1,1,0],[0,1,1,1],[1,1,1,0]]]
]
solution = Solution()
for expected, mat in test_cases:
    actual = solution.numSubmat(mat)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: mat: {mat}")

print("Ran all tests")