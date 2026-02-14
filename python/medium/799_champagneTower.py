class Solution:
    # Just do the calculations up til the query
    # Time O(1) really it's O(query_row)
    # Space O(1) Really it's O(102)
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize tower with everything to 0 except for first glass to all
        tower = [[0.0] * k for k in range(1, 102)]
        tower[0][0] = poured

        # Loop through all the rows until we compute the query row fully
        for row in range(query_row + 1):
            for col in range(len(tower[row])):
                # Determine overflow from cup above
                overflow = (tower[row][col] - 1.0) / 2.0

                # Put the overflow into the cups beneath it
                if overflow > 0:
                    tower[row+1][col] += overflow
                    tower[row+1][col+1] += overflow

        # Could be overflowing in final row too, so cap at 1
        return min(1, tower[query_row][query_glass])

testCases = [
    [1, 1, 1, 0],
    [2, 1, 1, .5],
    [100000009, 33, 17, 1]
]
implementation = Solution()
for poured, row, col, expected in testCases:
    answer = implementation.champagneTower(poured, row, col)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. Poured: {poured}, row: {row}, col: {col}")

print("Ran all tests")
