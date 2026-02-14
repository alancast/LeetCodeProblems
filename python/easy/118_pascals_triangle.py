class Solution:
    # Time O(num_rows^2)
    # Space O(1) no space other than answer
    def generate(self, numRows: int) -> list[list[int]]:
        answer = []

        for i in range(numRows):
            current_row = [1] * (i + 1)
            for j in range(1, i):
                current_row[j] = answer[-1][j-1] + answer[-1][j]

            answer.append(current_row)

        return answer

test_cases = [
    [[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], 5],
    [[[1]], 1]
]
solution = Solution()
for expected, num_rows in test_cases:
    actual = solution.generate(num_rows)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: num_rows: {num_rows}")

print("Ran all tests")
