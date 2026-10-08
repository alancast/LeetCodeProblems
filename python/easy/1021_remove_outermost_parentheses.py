class Solution:
    # Go over string once, count level, and only add to answer if level > 0
    # Time O(n)
    # Space O(1) just answer string
    def removeOuterParentheses(self, s: str) -> str:
        answer, level = [], 0

        # Go over whole string
        for char in s:
            if char == ")":
                level -= 1
            if level > 0:
                answer.append(char)
            if char == "(":
                level += 1

        return "".join(answer)

test_cases = [
    ["()()()", "(()())(())"],
    ["()()()()(())", "(()())(())(()(()))"],
    ["", "()()"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.removeOuterParentheses(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
