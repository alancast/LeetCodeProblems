class Solution:
    # Count open and close parentheses in both directions
    # This avoids extra space and can find valid substrings across the string
    # Time O(n)
    # Space O(1)
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        left = 0
        right = 0

        # First pass: count matches from left to right
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                answer = max(answer, left * 2)
            elif right > left:
                left = 0
                right = 0

        # Reset counts and scan right to left for matches missed by the first pass
        left = 0
        right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                answer = max(answer, left * 2)
            elif left > right:
                left = 0
                right = 0

        return answer

test_cases = [
    [2, "(()"],
    [4, ")()())"],
    [0, ""]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.longestValidParentheses(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
