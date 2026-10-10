class Solution:
    # Greedily match each closing bracket with an open one when possible.
    # Time O(n)
    # Space O(1)
    def minInsertions(self, s: str) -> int:
        length = len(s)
        insertions = left_count = index = 0

        while index < length:
            # If we see an opening bracket, keep it as an unmatched left side.
            if s[index] == "(":
                left_count += 1
                index += 1
            else:
                # If there is an unmatched opening bracket, use it to match this closing bracket.
                if left_count > 0:
                    left_count -= 1
                # Otherwise, we are missing a left side before this closing bracket.
                else:
                    insertions += 1

                # If the next character is another closing bracket, we can match the current
                # closing bracket with a pair of close brackets using the minimum extra work.
                if index < length - 1 and s[index + 1] == ")":
                    index += 2
                # If the next character is not a closing bracket, we need to add one more
                # opening bracket before the current closing bracket to make the structure valid.
                else:
                    insertions += 1
                    index += 1

        # Any remaining unmatched opening brackets must each be closed with two insertions.
        insertions += left_count * 2
        return insertions

test_cases = [
    [1, "(()))"],
    [0, "())"],
    [3, "))())("]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.minInsertions(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
