class Solution:
    def isValid(self, s: str) -> bool:
        closingsMap = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        
        stack = []
        for char in s:
            if char not in closingsMap:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                lastChar = stack.pop()
                if closingsMap[char] != lastChar:
                    return False

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