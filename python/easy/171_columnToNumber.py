class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        exponent = len(columnTitle) - 1
        for char in columnTitle:
            letterIndex = ord(char) - ord('A') + 1
            num += letterIndex * (26**exponent)
            exponent -= 1

        return num

testCases = [
    ["A", 1],
    ["AA", 27],
    ["ZY", 701]
]
implementation = Solution()
for column, expected in testCases:
    answer = implementation.titleToNumber(column)
    if answer != expected:
        print(f"FAILED TEST: Got {answer}, but expected {expected}. INPUT: {column}")