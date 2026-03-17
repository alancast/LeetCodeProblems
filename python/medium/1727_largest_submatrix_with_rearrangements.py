class Solution:
    # Turns out possible to do without sorting rows
    # If we strategically append to a heights tracker it is always sorted
    # Without needing to actually sort
    # Time O(mn)
    # Space O(n)
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        # Stores tuples of (height, col_index)
        # Because of how we append to this it will always be sorted
        prev_heights = []

        answer = 0
        # Go row by row and compute max area from that row
        for row in range(rows):
            heights = []
            # Mark what columns we've visited due to previous heights
            seen = [False] * cols

            # Go over all previous heights and see if any continue
            for height, col in prev_heights:
                if matrix[row][col] == 1:
                    heights.append((height + 1, col))
                    seen[col] = True

            # Go over all unseen cols and see if we have new heights to add
            for col in range(cols):
                if not seen[col] and matrix[row][col] == 1:
                    heights.append((1, col))

            # Because of how we append to this it will always be sorted
            for i in range(len(heights)):
                # Lowest height times width (+1 cuz zero indexed)
                answer = max(answer, heights[i][0] * (i + 1))

            prev_heights = heights

        return answer

    # Same method as below but doesn't modify input
    # Time O(mnlogn)
    # Space O(n) for sort
    def largestSubmatrix_sort(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prev_row = [0] * cols

        answer = 0
        # Count consecutive ones and update prev row
        # After completing each row compute max area we can find
        for row in range(rows):
            curr_row = matrix[row][:]
            for col in range(cols):
                if curr_row[col] != 0:
                    curr_row[col] += prev_row[col]

            # Sort the current row and find the max area
            sorted_row = sorted(curr_row, reverse=True)
            for col in range(cols):
                # Lowest height times width (+1 cuz zero indexed)
                answer = max(answer, sorted_row[col] * (col + 1))

            # Update previous row
            prev_row = curr_row

        return answer

    # Create matrix of number of ones in a column (top to bottom)
    # Sort that for each row and find answers
    # Time O(mnlogn)
    # Space O(n) for sort
    def largestSubmatrix_modify_input(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        answer = 0
        # Modify matrix to store consecutive ones
        # After completing each row compute max area we can find
        for row in range(rows):
            for col in range(cols):
                # Update value to add consecutive ones
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            # Sort the current row and find the max area
            curr_row = sorted(matrix[row], reverse=True)
            for col in range(cols):
                # Lowest height times width (+1 cuz zero indexed)
                answer = max(answer, curr_row[col] * (col + 1))

        return answer

test_cases = [
    [4, [[0,0,1],[1,1,1],[1,0,1]]],
    [3, [[1,0,1,0,1]]],
    [2, [[1,1,0],[1,0,1]]]
]
solution = Solution()
for expected, matrix in test_cases:
    actual = solution.largestSubmatrix(matrix)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: matrix: {matrix}")

print("Ran all tests")
