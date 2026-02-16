class Solution:
    # Just check squares
    # Time O(n^2)
    # Space O(1)
    def validWordSquare(self, words: list[str]) -> bool:
        n = len(words)

        for word_num in range(n):
            for char_pos in range(len(words[word_num])):
                # char_pos (curr 'row' word) is bigger than column word, or
                # word_num (curr 'column' word) is bigger than row word, or
                # characters at index (word_num,char_pos) and (char_pos,word_num) are not equal.
                if char_pos >= len(words) or \
                    word_num >= len(words[char_pos]) or \
                    words[word_num][char_pos] != words[char_pos][word_num]:
                    return False

        # All checked so same
        return True

test_cases = [
    [True, ["abcd","bnrt","crmy","dtye"]],
    [True, ["abcd","bnrt","crm","dt"]],
    [False, ["ball","area","read","lady"]]
]
solution = Solution()
for expected, words in test_cases:
    actual = solution.validWordSquare(words)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: words: {words}")

print("Ran all tests")
