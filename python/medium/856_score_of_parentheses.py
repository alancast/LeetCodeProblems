class Solution:
    # Use math keeping track of balance and summing powers of two
    # Time O(n)
    # Space O(1)
    def scoreOfParentheses(self, s: str) -> int:
        answer = balance = 0

        # Go over chars and keep track of balance
        for index, char in enumerate(s):
            if char == '(':
                balance += 1
            else:
                balance -= 1
                if s[index-1] == '(':
                    answer += 1 << balance

        return answer

    # Use a stack to keep track of current score
    # Time O(n)
    # Space O(n)
    def scoreOfParentheses_stack(self, s: str) -> int:
        # The score of the current frame
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

test_cases = [
    [1, "()"],
    [2, "(())"],
    [2, "()()"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.scoreOfParentheses(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
