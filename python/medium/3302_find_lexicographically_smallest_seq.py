class Solution:
    # Time O(n+m)
    # Space O(m)
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        last = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        answer = []
        skip = j = 0
        for i, c in enumerate(word1):
            if j == m:
                break
            if c == word2[j] or (skip == 0 and (j == m - 1 or i < last[j + 1])):
                skip += c != word2[j]
                answer.append(i)
                j += 1

        return answer if j == m else []

test_cases = [
    [[0,1,2], "vbcca", "abc"],
    [[1,2,4], "bacdc", "abc"],
    [[], "aaaaaa", "aaabc"]
]
solution = Solution()
for expected, word_1, word_2 in test_cases:
    actual = solution.validSequence(word_1, word_2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: word_1: {word_1}, word_2: {word_2}")

print("Ran all tests")
