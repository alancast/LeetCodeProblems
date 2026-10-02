class Solution:
    # Backtracking solution to generate all valid parentheses combinations.
    # Time O(4^n / sqrt(n)) - Catalan number growth
    # Space O(n) for the recursion stack and the answer list
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return [""]

        answer = []
        for left_count in range(n):
            left_strings = self.generateParenthesis(left_count)
            right_strings = self.generateParenthesis(n - 1 - left_count)
            for left_string in left_strings:
                for right_string in right_strings:
                    answer.append("(" + left_string + ")" + right_string)

        return answer

test_cases = [
    [["((()))","(()())","(())()","()(())","()()()"], 3],
    [["()"], 1]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.generateParenthesis(n)
    if set(expected) != set(actual):
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
