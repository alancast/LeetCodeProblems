class Solution:
    # Just go over all words and see if column is deleted
    # Time O(n*m)
    # Space O(1)
    def minDeletionSize(self, strs: list[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        answer = 0

        for col in range(cols):
            prev_char = strs[0][col]
            for row in range(1, rows):
                char = strs[row][col]
                if char < prev_char:
                    answer += 1
                    break

                prev_char = char

        return answer

test_cases = [
    [1, ["bca", "daf", "ghi"]],
    [0, ["a", "a"]],
    [0, ["a", "b"]],
    [3, ["zyx", "wvu", "tsr"]]
]
solution = Solution()
for expected, strs in test_cases:
    actual = solution.minDeletionSize(strs)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: strs: {strs}")

print("Ran all tests")
