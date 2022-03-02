class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0
        end = len(s)
        for letter in t:
            if letter == s[i]:
                i += 1
            
            if i == end:
                return True

        return False

testCases = [
    ["s", "t", False],
    ["s", "s", True],
    ["", "t", True],
    ["abc", "ahbgdc", True],
    ["acb", "ahbgdc", False],
    ["axc", "ahbgdc", False],
]
implementation = Solution()
for s, t, expected in testCases:
    answer = implementation.isSubsequence(s, t)
    if answer != expected:
        print(f"FAILED TEST: got {answer}, expected {expected}. S: {s}, t: {t}")