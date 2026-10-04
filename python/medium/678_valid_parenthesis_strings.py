class Solution:
    # Two pointers, one on each end checking for count
    # Time O(n)
    # Space O(1)
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        length = len(s) - 1

        # Traverse the string from both ends simultaneously
        for i in range(length + 1):
            # Count open parentheses or asterisks
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1

            # Count close parentheses or asterisks
            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1

            # If at any point open count or close count goes negative, the string is invalid
            if open_count < 0 or close_count < 0:
                return False

        # If open count and close count are both non-negative, the string is valid
        return True

test_cases = [
    [True, "()"],
    [True, "(*)"],
    [True, "(*))"],
    [False, "("]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.checkValidString(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
