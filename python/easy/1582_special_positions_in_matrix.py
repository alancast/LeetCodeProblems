class Solution:
    # Go over matrix twice.
    # First pass keep array of row count and col count
    # Second pass see if row and col count 1
    # Time O(nm)
    # Space O(n + m)
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        row_count = [0] * rows
        col_count = [0] * cols

        # Go over matrix and update counts
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1

        # Go over second time and find specials
        answer = 0
        for row in range(rows):
            # Nothing in this row is special
            if row_count[row] > 1:
                continue

            for col in range(cols):
                # We found the only one in the row, see if it's special then break
                if mat[row][col] == 1:
                    answer += col_count[col] == 1
                    break

        return answer

test_cases = [
    [1, [[1,0,0],[0,0,1],[1,0,0]]],
    [3, [[1,0,0],[0,1,0],[0,0,1]]]
]
solution = Solution()
for expected, mat in test_cases:
    actual = solution.numSpecial(mat)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: mat: {mat}")

print("Ran all tests")
