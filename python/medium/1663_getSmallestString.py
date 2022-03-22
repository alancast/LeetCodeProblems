class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        chars = []

        while n > 0:
            maxLeft = (n-1) * 26
            if maxLeft >= k:
                chars.append('a')
                k -= 1
            elif k - maxLeft < 26:
                chars.append(chr(96 + k - maxLeft))
                k -= (k - maxLeft)
            else:
                chars.append('z')
                k -= 26

            n -= 1

        return ''.join(chars)

testCases = [
    [3, 27, "aay"],
    [5, 73, "aaszz"]
]
implementation = Solution()
for n, k, expected in testCases:
    answer = implementation.getSmallestString(n, k)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: n: {n} k: {k}")