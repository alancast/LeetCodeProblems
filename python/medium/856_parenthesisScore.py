class Solution:
    # Stack solution, always keep score in the stack
    # We know it'll end with 1 item because it's balanced
    # O(n) time and space
    def scoreOfParenthesesStack(self, s: str) -> int:
        stack = [0]

        for x in s:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

    # Use math keeping track of balance and summing powers of two
    # O(n) time O(1) space
    def scoreOfParentheses(self, s: str) -> int:
        ans = bal = 0
        for i, x in enumerate(s):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if s[i-1] == '(':
                    ans += 1 << bal
        return ans

testCases = [
    ["()", 1],
    ["()()", 2],
    ["(())", 2],
    ["((())())", 6]
]
implementation = Solution()
for s, expected in testCases:
    answer = implementation.scoreOfParentheses(s)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {s}")