class Solution:
    # Keep a stack with opening and closing parentheses and use to validate
    # Time O(n)
    # Space O(n)
    def isValid(self, s: str) -> bool:
        # What each closing maps to with it's opening
        closingsMap = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        # Keep track of any openings we see
        # and when we see a closing make sure it's opening is top of stack
        stack = []
        for char in s:
            # Not a closing so add to stack
            if char not in closingsMap:
                stack.append(char)
            # Is a closing, so make sure valid opening before
            else:
                if len(stack) == 0:
                    return False

                lastChar = stack.pop()
                if closingsMap[char] != lastChar:
                    return False

        # Make sure stack is empty at the end, meaning all openings had closings
        return len(stack) == 0

testCases = [
    ["", True],
    ["[]", True],
    ["(", False],
    [")", False],
    ["()[]{}", True],
    ["([]{})", True],
    ["(]", False]
]
implementation = Solution()
for s, expected in testCases:
    answer = implementation.isValid(s)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {s}")

print("Ran all tests")
