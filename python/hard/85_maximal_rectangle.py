from typing import List


class Solution:
    # At each point compute height of rectangle, then go left and right
    # Time O(nm)
    # Space O(m)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        left = [0] * cols
        right = [cols] * cols
        height = [0] * cols

        answer = 0

        for row in range(rows):
            cur_left = 0
            cur_right = cols

            # update height of each col
            for col in range(cols):
                if matrix[row][col] == '1':
                    height[col] += 1
                else:
                    height[col] = 0

            # update index with leftmost index of that height
            for col in range(cols):
                if matrix[row][col] == '1':
                    left[col] = max(left[col], cur_left)
                else:
                    # Reset it to max width as we start new height count
                    left[col] = 0
                    cur_left = col + 1

            # update index with rightmost index of that height
            for col in range(cols-1, -1, -1):
                if matrix[row][col] == '1':
                    right[col] = min(right[col], cur_right)
                else:
                    # Reset it to max width as we start new height count
                    right[col] = cols
                    cur_right = col

            # Go over all cols and find the max area
            for col in range(cols):
                answer = max(answer, height[col] * (right[col] - left[col]))

        return answer

    # Utilize finding max area in a histogram of heights
    # Go over row by row and convert to a histogram of heights for each row
    # Time O(nm)
    # Space O(nm)
    def maximalRectangleHist(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        maxarea = 0
        # Height of 1s in the column
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # update the state of cols histogram using the last row's histogram
                # by keeping track of the number of consecutive ones
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # update maxarea with the maximum area from this row's histogram
            maxarea = max(maxarea, self.leetcode84(dp))

        return maxarea

    # Get the maximum area in a histogram given its heights
    # Find the max area of a rectangle when it's a histogram of heights
    def leetcode84(self, heights):
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))

            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))

        return maxarea

    # Use DP array of width of ones at that row
    # Go over indexes and see what max area is
    # Time O(n^2*m)
    # Space O(nm)
    def maximalRectangle_dp(self, matrix: List[List[str]]) -> int:
        maxarea = 0

        # DP of how many 1's to left at that index
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                # Go up to top and find min width and height
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
    
        return maxarea

    # Go over all squares and if it's a 1 start a search
    # Takes too long
    def maximalRectangle_TLE(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1

                # compute the max area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))

        return maxarea

test_cases = [
    [6, [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]],
    [0, [["0"]]],
    [1, [["1"]]]
]
solution = Solution()
for expected, matrix in test_cases:
    actual = solution.maximalRectangle(matrix)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: matrix: {matrix}")

print("Ran all tests")
