from collections import Counter


class Solution:
    # Could be more optimized by moving the window boundaries
    # until the offending dupe is gone. But eh 🤷‍♂️ not doing it
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0

        count = 0
        chars = Counter(s[:k])
        for i in range(k, len(s)):
            if len(chars) == k:
                count += 1
            addingChar = s[i]
            removingChar = s[i-k]

            chars[removingChar] -= 1
            if chars[removingChar] == 0:
                del chars[removingChar]
            chars[addingChar] = chars.get(addingChar, 0) + 1

        # Check the final set to see if last k chars count
        if len(chars) == k:
            count += 1

        return count

testCases = [
    ["havefunonleetcode", 5, 6],
    ["a", 2, 0],
    ["abcde", 1, 5],
    ["abcde", 2, 4],
    ["aabcde", 1, 6],
    ["aabcde", 2, 4]
]
solution = Solution()
for s, k, expected in testCases:
    answer = solution.numKLenSubstrNoRepeats(s, k)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. INPUTS: s: {s}, k: {k}")